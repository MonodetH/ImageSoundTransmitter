import pyaudio

from matplotlib import pyplot as plt

from Source.IO.Sync import *
import numpy as np
import wave
from scipy import signal

CHUNKSIZE = int(44100//0.25)  # fixed chunk size
sync = createSyncSignal()
success = createSuccessSignal()
error = createErrorSignal()

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

print("Esperando señal")

#####
# Ahora abrir el audio llamado syncSignal
#####
while(True):
    data = stream.read(CHUNKSIZE)
    numpydata = np.fromstring(data, dtype=np.int16)

    delay = findSyncSignal(numpydata, sync)
    if(delay):
        print("Sync encontrado!")
        stream.read(delay)
        break

direccion = "../Resources/Audio/Created/testRecord.wav"

frames = []

duracion = 5

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

print("Grabando")

for i in range(0, int(RATE / CHUNK * duracion)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Terminado")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(direccion, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

