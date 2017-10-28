import pyaudio
import wave
from Source.IO.ReadAudio import readAudio
from Source.Modulation.Correlation import correlation

input("Pulsa enter para iniciar grabación...")

direccion = "../Resources/Audio/Created/testRecordDemod.wav"
#duracion en segundos
duracion = 18

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Grabando")

frames = []

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



data1, frameRate1 = readAudio(direccion)

fs = 44100                     #frecuencia de muestreo
T = 0.5                         #tiempo de bit
fr1 = 6000                      #frecuencia 1
fr2 = 9000                   #frecuencia 2
a1 = 0
data_img_demod = correlation(data1, fr1, fr2, fs, len(data1), a1, T)

print(data_img_demod)