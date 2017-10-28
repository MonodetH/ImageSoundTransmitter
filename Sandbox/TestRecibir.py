import numpy as np
import pyaudio

from Source.IO.Sync import *
from Source.IO.WriteImage import writeImageBN
from Source.Modulation.Correlation import correlateBank, correlationToData

SIGNAL_CHUNK_SIZE = 44100  # fixed chunk size
DATA_CHUNK_SIZE = 44100
FRAMERATE = 44100

sync = createSyncSignal()
success = createSuccessSignal()
error = createErrorSignal()

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=FRAMERATE, input=True, frames_per_buffer=DATA_CHUNK_SIZE)

print("Esperando señal")

simbolosPorRecibir = 4
bitsPerSimbol = 8
baudRate = 5

framesPerSimbol = int(FRAMERATE / baudRate)

frames = []
while(True):
    data = stream.read(SIGNAL_CHUNK_SIZE)
    numpydata = np.fromstring(data, dtype=np.int16)

    delay = findSyncSignal(numpydata, sync)
    if(delay):
        print("Sync encontrado!")
        delay += 5512+2756+1000+800
        desfase = SIGNAL_CHUNK_SIZE - delay
        if(desfase<0):
            stream.read(-desfase)
        else:
            print("Faltan", simbolosPorRecibir, "simbolos")
            while(desfase>framesPerSimbol):
                frames.extend(numpydata[delay:delay+framesPerSimbol])
                delay += framesPerSimbol
                desfase -= framesPerSimbol
                simbolosPorRecibir -= 1
                if simbolosPorRecibir == 0:
                    break
            if simbolosPorRecibir == 0:
                break
            frames.extend(numpydata[-desfase:])
            data = stream.read(framesPerSimbol-desfase)
            frames.extend(np.fromstring(data, dtype=np.int16))
            simbolosPorRecibir -= 1
        break


print("Grabando")

for i in range(0, simbolosPorRecibir):
    data = stream.read(framesPerSimbol)
    frames.extend(np.fromstring(data, dtype=np.int16))

stream.stop_stream()
stream.close()
p.terminate()

print("Procesando")

#spectrogram(frames,44100)
#plotFFT(frames,44100,"fft")

correlationData = correlateBank(frames, bitsPerSimbol, 15000, 20000, baudRate=baudRate)
data = correlationToData(correlationData, bitsPerSimbol, baudRate)


# framesPerSimbol = int(simbolDuration*FRAMERATE)
# frameSnap = int(framesPerSimbol/2)
# data = []
# for i in range(0,int(duracion/simbolDuration)):
#     #print(correlationData[0][frameSnap], correlationData[1][frameSnap])
#     #data.extend(np.argmax([max(correlationData[0][frameSnap:frameSnap+5]), max(correlationData[1][frameSnap:frameSnap+5])]))
#     if(correlationData[0][frameSnap]>correlationData[1][frameSnap]):
#         data.extend([0])
#     else:
#         data.extend([1])
#     #data.extend(np.argmax(np.array([correlationData[0][frameSnap], correlationData[1][frameSnap]])))
#     frameSnap += framesPerSimbol

# plt.subplot(2,1,1)
# plt.plot(correlationData[0])
# plt.subplot(2,1,2)
# plt.plot(correlationData[1])
# plt.show()

print(data)

#writeImageBN(data,(2,2),"../Resources/Sample Images/testIMG4_2x2.jpg")