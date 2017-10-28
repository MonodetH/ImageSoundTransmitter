from Source.IO.Sync import *
from Source.Modulation.Digital import MFSK
from Source.IO.Sync import createSyncSignal
from Source.Modulation.Correlation import correlateBank, correlationToData, getNormas
import pyaudio
import numpy as np
import itertools


def sendData(data,bitsPerSimbol,baudRate):
    sync = createSyncSignal()
    datos = np.append(sync, MFSK(data, bitsPerSimbol, 15000, 20000,baudRate=baudRate))

    CHUNK = 1024
    FRAMERATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=FRAMERATE,
                    output=True)

    streamData = datos.astype(np.float32).tostring()
    stream.write(streamData)
    stream.stop_stream()
    stream.close()
    p.terminate()

def receiveData(frameLenght,bitsPerSimbol,baudRate,norm=None):
    SIGNAL_CHUNK_SIZE = 44100  # fixed chunk size
    DATA_CHUNK_SIZE = 44100
    FRAMERATE = 44100

    sync = createSyncSignal()

    # initialize portaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=FRAMERATE, input=True, frames_per_buffer=DATA_CHUNK_SIZE)

    print("Esperando señal")

    framesPerSimbol = int(FRAMERATE / baudRate)

    frames = []
    while (True):
        data = stream.read(SIGNAL_CHUNK_SIZE)
        numpydata = np.fromstring(data, dtype=np.int16)

        delay = findSyncSignal(numpydata, sync)
        if (delay):
            print("Sync encontrado!")
            delay += 5512 + 2756 + 1000 + 800  # Una sincronizacion muy fina
            desfase = SIGNAL_CHUNK_SIZE - delay
            if (desfase < 0):
                stream.read(-desfase)
            else:
                while (desfase > framesPerSimbol):
                    frames.extend(numpydata[delay:delay + framesPerSimbol])
                    delay += framesPerSimbol
                    desfase -= framesPerSimbol
                    frameLenght -= 1
                    if frameLenght == 0:
                        break
                if frameLenght == 0:
                    break
                frames.extend(numpydata[-desfase:])
                data = stream.read(framesPerSimbol - desfase)
                frames.extend(np.fromstring(data, dtype=np.int16))
                frameLenght -= 1
            break

    print("Grabando")

    for i in range(0, frameLenght):
        data = stream.read(framesPerSimbol)
        frames.extend(np.fromstring(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Procesando")

    correlationData = correlateBank(frames, bitsPerSimbol, 15000, 20000, baudRate=baudRate)
    norm = getNormas(correlationData,bitsPerSimbol)
    data = correlationToData(correlationData, bitsPerSimbol, baudRate,norm=norm)

    print(data)
    return data


def sendSimbols(bitsPerSimbol):
    duracionEnvio = 10
    baudRate = int(2**bitsPerSimbol / duracionEnvio)

    preData = list(map(list, itertools.product([0, 1], repeat=bitsPerSimbol)))
    data = [item for sublist in preData for item in sublist]
    print(data)
    sendData(data,bitsPerSimbol,baudRate)


def receiveNorm(bitsPerSimbol):
    duracionEnvio = 10
    cantSimbolos = 2 ** bitsPerSimbol
    baudRate = int(cantSimbolos / duracionEnvio)

    SIGNAL_CHUNK_SIZE = 44100  # fixed chunk size
    DATA_CHUNK_SIZE = 44100
    FRAMERATE = 44100

    sync = createSyncSignal()

    # initialize portaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=FRAMERATE, input=True, frames_per_buffer=DATA_CHUNK_SIZE)

    print("Esperando señal")

    framesPerSimbol = int(FRAMERATE / baudRate)

    frames = []
    while (True):
        data = stream.read(SIGNAL_CHUNK_SIZE)
        numpydata = np.fromstring(data, dtype=np.int16)

        delay = findSyncSignal(numpydata, sync)
        if (delay):
            print("Sync encontrado!")
            break

    print("Grabando")

    for i in range(0, 11):
        data = stream.read(FRAMERATE)
        frames.extend(np.fromstring(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Obteniendo perfil de sonido")

    correlationData = correlateBank(frames, bitsPerSimbol, 15000, 20000, baudRate=baudRate)
    normas = getNormas(correlationData,bitsPerSimbol)

    return normas


def sendResponse(success=True):
    sync = []
    if success:
        sync = createSuccessSignal()
    else:
        sync = createErrorSignal()
    datos = sync

    CHUNK = 1024
    FRAMERATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=FRAMERATE,
                    output=True)

    streamData = datos.astype(np.float32).tostring()
    stream.write(streamData)
    stream.stop_stream()
    stream.close()
    p.terminate()


def waitResponse():
    CHUNKSIZE = int(44100 // 0.25)  # fixed chunk size
    sync = createSyncSignal()
    success = createSuccessSignal()
    error = createErrorSignal()

    # initialize portaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

    print("Escuchando señal")

    #####
    # Ahora abrir un audio llamado syncSignal, successSignal o errorSignal
    #####

    signal = -1
    while (True):
        data = stream.read(CHUNKSIZE)
        numpydata = np.fromstring(data, dtype=np.int16)

        signal = findResponseSignals(numpydata,success, error)
        if (signal == 0):
            print("Success encontrado!")
            break
        if (signal == 1):
            print("Error encontrado!")
            break

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    return signal
