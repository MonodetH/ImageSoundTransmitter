# coding=utf-8
from Source.Filter.Butterworth import *
from Source.IO.ReadAudio import readAudio
from Source.IO.WriteAudio import writeAudio
from Source.Plot.PlotFFT import plotFFT
from Source.Plot.PlotSignal import plotSignal
from Source.Plot.Spectrogram import spectrogram
from Source.Tools.FFT import *
from Source.Tools.SignalFactory import sinFactory

# Primer experimento: Leer archivo y graficar señal, FFT, espectrograma, FFT post filtro y espectrograma post filtro.
# Se lee los datos de la señal.
inputFile = "../Resources/Audio/ask-snr=10.wav"
data1, frameRate1 = readAudio(inputFile)

# Grafico de la señal.
plotSignal(data1, frameRate1)

# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFT(data1,frameRate1, "FFT de la señal ingresada")

# Grafico del espectrograma de la señal.
spectrogram(data1,frameRate1)

# Se obtiene la frecuencia de mayor peso
frecMax = findMaxFreq(data1,frameRate1)

# Se aplica filtro a la señal.
data1_filtered = butterPasabanda(data1,frecMax-25,frecMax+25,frameRate1)

# Se vuelven a realizar los graficos, pero con la señal filtrada.
plotSignal(data1_filtered, frameRate1, image="PlotSignal_filtered")
plotFFT(data1_filtered,frameRate1, "FFT señal filtrada", image="PlotFFT_filtered")
spectrogram(data1_filtered,frameRate1, image="Spectrogram_filtered")

# Segundo experimento: Escribir archivo con una señal y luego graficar la señal, FFT y espectrograma.
# Se escribe el archivo con una señal: cos(2*pi*freq*t/frameRate)
outputFile = "../Resources/Audio/Created/sample.wav"
freq2 = 440.0
frameRate2 = 44100 # frameRate de todos los archivos
time2 = 5   # en segundos
writeAudio(outputFile, sinFactory(freq2, frameRate2, time2), frameRate2)

# Se lee los datos de la señal.
data2, frameRate2 = readAudio(outputFile)    # Se lee la señal recien creada

# Grafico de la señal.
plotSignal(data2, frameRate2, image="PlotSignal_created")
# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFT(data2,frameRate2, "FFT de la señal creada", image="PlotFFT_created")
# Grafico del espectrograma de la señal.
spectrogram(data2,frameRate2, image="Spectrogram_created")