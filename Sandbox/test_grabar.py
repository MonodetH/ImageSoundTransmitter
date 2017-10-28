#https://www.howtoinstall.co/es/ubuntu/trusty/python3-pyaudio
import pyaudio

import wave

import matplotlib.pyplot as plt
from Source.IO.ReadAudio import readAudio
from Source.IO.WriteAudio import writeAudio
from Source.Plot.PlotFFT import plotFFT
from Source.Plot.PlotFFT import plotFFTLog
from Source.Plot.PlotSignal import plotSignal
from Source.Plot.Spectrogram import spectrogram

from Source.Tools.SignalFactory import cosCreciente
#
#creando cos
#
#test_cos = cosFactory(20000,44100,15)
#test_cos_creciente = cosCreciente(44100, 10)
#writeAudio("../Resources/Audio/Created/test_record_cos.wav",test_cos_creciente,44100)
#plotFFT(test_cos_creciente, 44100, "FFT", image="FFT_cos_creciente")
#spectrogram(test_cos_creciente, 44100, image="Spectrograma_cos_creciente")


#antes de pulsar enter abrir el archivo test_record_cos.wav
input("Pulsa enter para continuar...")

#
#grabando
#

direccion = "../Resources/Audio/Created/testRecord.wav"
#duracion en segundos
duracion = 10

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


# Grafico de la señal.
plotSignal(data1, frameRate1)

# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFTLog(data1,frameRate1, "FFT de la señal ingresada")

