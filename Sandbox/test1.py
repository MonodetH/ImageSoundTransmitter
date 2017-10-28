from Source.Plot.PlotFFT import plotFFT
from Source.Plot.PlotSignal import plotSignal
from Source.Plot.Spectrogram import spectrogram
from Source.Tools.FFT import findMaxFreq

# Primer experimento: Leer archivo y graficar señal, FFT, espectrograma, FFT post filtro y espectrograma post filtro.
# Se lee los datos de la señal.
inputFile = "../Resources/Audio/ook.wav"
data1, frameRate1 = read(inputFile)

# Grafico de la señal.
plotSignal(data1, frameRate1)
# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFT(data1)
# Grafico del espectrograma de la señal.
spectrogram(data1,frameRate1)

frecMax = (int)(findMaxFreq(data1,frameRate1))

print(frecMax)

# Se aplica filtro a la señal.
#data1_filtered = ButterworthFilter(data1, frecMax)
data1_filtered = butter_bandpass_filter(data1,frecMax-100,frecMax+100,frameRate1)

# Se vuelven a realizar los graficos, pero con la señal filtrada.
plotSignal(data1_filtered, frameRate1)
plotFFT(data1_filtered)
spectrogram(data1_filtered,frameRate1)

# Segundo experimento: Escribir archivo con una señal y luego graficar la señal, FFT y espectrograma.
# Se escribe el archivo con una señal: cos(2*pi*freq*t/frameRate)
outputFile = "../Resources/Audio/Created/sample.wav"
freq2 = 440.0
frameRate2 = 44100 # frameRate de todos los archivos
time2 = 5   # en segundos
write(outputFile, freq2, frameRate2, time2)

# Se lee los datos de la señal.
data2, frameRate2 = read(outputFile)    # Se lee la señal recien creada

# Grafico de la señal.
plotSignal(data2, frameRate2)
# Grafico de la Transformada de Fourier(FFT) de la señal.
plotFFT(data2)
# Grafico del espectrograma de la señal.
spectrogram(data2,frameRate2)