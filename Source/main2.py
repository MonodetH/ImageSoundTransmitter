import matplotlib.pyplot as plt
import numpy as np
from Source.IO.ReadImage import readImageBN
from Source.Tools.intToBin import intToBin
from Source.Tools.ArrayToSignal import arrayToSignal
from Source.IO.WriteAudio import writeAudio
from Source.Tools.SignalFactory import cosFactory
from Source.Modulation.Analog import amMod
from Source.Modulation.Analog import amDemod
from Source.Plot.PlotFFT import plotFFT

#Parte 1: Lectura de imagen en bits

#Lectura de imagen en frames
img = readImageBN("../Resources/Sample Images/testIMG.jpg")
#Transformación de frames a su representación en bits
img_bin = intToBin(img, 8)
#Paso de bits a señal
img_signal, frameRate = arrayToSignal(img_bin, 4, 44100)
#Modulación de señal a frecuencia audible
am_imgSignal = amMod(img_signal, frameRate, 440.0)
#Escritura de archivo .wav con la señal modulada
writeAudio("../Resources/Audio/Created/testImg.wav", am_imgSignal, frameRate)

#Parte 2: Modulación

# constantes
fr = 44100
duration = 0.1
origFreq = 500
objFreq = 2000
# Modulacion
vx = cosFactory(origFreq,fr,duration)

cantMuestra2 = len(vx)
t = np.linspace(0,duration,cantMuestra2)# duracion de 1 segundo con numero de muestras cantMuestra

plt.subplot(3,1,1)
#plt.title("Señal Moduladora", y=1.08)
plt.plot(t,vx)


y1 = cosFactory(objFreq,fr,duration)
plt.subplot(3,1,2)
#plt.title("Señal Portadora", y=1.08)
plt.plot(t,y1)


mod = amMod(vx,fr,objFreq)
plt.subplot(3,1,3)
#plt.title("Señal Modulada", y=1.08)
plt.plot(t,mod)

plt.savefig("../Resources/Images/Modulacion.png")
plt.show()



# Demodulacion
plt.subplot(2,1,1)
#plt.title("Señal Modulada", y=1.08)
plt.plot(t,mod)

demod = amDemod(mod,fr,objFreq)
plt.subplot(2,1,2)
#plt.title("Señal Demodulada", y=1.08)
plt.plot(t,demod)

plt.savefig("../Resources/Images/Demodulacion.png")
plt.show()

#FFT
plotFFT(vx,fr, "FFT Señal Original", "FFTModOriginal")

plotFFT(mod,fr, "FFT Señal Modulada", "FFTModModulada")

plotFFT(demod,fr, "FFT Señal Demodulada", "FFTModDemodulada")


