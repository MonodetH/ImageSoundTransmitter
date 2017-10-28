from Source.Filter.Butterworth import *
from Source.Plot.PlotFFT import plotFFT
from Source.Plot.PlotSignal import plotSignal
from Source.Plot.Spectrogram import spectrogram
from Source.Tools.FFT import findMaxFreq

# Primer experimento: Leer archivo y graficar señal, FFT, espectrograma, FFT post filtro y espectrograma post filtro.
# Se lee los datos de la señal.
inputFile = "../Resources/Audio/ask-snr=10.wav"
data1, frameRate1 = read(inputFile)

# Grafico de la señal.
plotSignal(data1, frameRate1)
# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFT(data1, frameRate1)
# Grafico del espectrograma de la señal.
spectrogram(data1,frameRate1)

frecMax = (int)(findMaxFreq(data1,frameRate1))

print(frecMax)

# Se aplica filtro a la señal.
#data1_filtered = ButterworthFilter(data1, frecMax)
data1_filtered = butterPasabanda(data1,frecMax-25,frecMax+25,frameRate1)

# Se vuelven a realizar los graficos, pero con la señal filtrada.

print(len(data1))
print(len(data1_filtered))

plotSignal(data1_filtered, frameRate1, image="PlotSignal_filtered")
plotFFT(data1_filtered, frameRate1, image="PlotFFT_filtered")
spectrogram(data1_filtered,frameRate1, image="Spectrogram_filtered")