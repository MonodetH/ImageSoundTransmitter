import numpy as np
import matplotlib.pyplot as plt
from Source.Modulation.Digital import FSK
from Source.Modulation.Digital import ASK
from Source.IO.ReadImage import readImageBN
from Source.IO.WriteImage import writeImageBN
from Source.IO.WriteAudio import writeAudio
from Source.IO.ReadAudio import readAudio
from Source.Tools.intToBin import intToBin
#from Source.Modulation.Digital import demodBank
from Source.Modulation.Correlation import correlation

#Parametros
fs = 44100                     #frecuencia de muestreo
T = 0.5                     #tiempo de bit
fr1 = 6000                      #frecuencia 1
fr2 = 9000                   #frecuencia 2
a1 = 0                          #amplitud 1
a2 = 10                         #amplitud 2
tb = np.linspace(0, 1, fs*T)    #vector de tiempo
data0=[0]
data1=[1]
#Lectura de imagen en frames
img = readImageBN("../Resources/Sample Images/testIMG_2x2.jpg")
dim = (len(img), len(img[0]))  #Dimensiones de la imagen
#Transformación de frames a su representación en bits
img_bin = intToBin(img, 8)
#Stream de datos
stream_data = img_bin.ravel()
writeImageBN(stream_data, dim, "../Resources/Sample Images/saved.jpg")

#stream_data = [0,1,0,1]
#t = np.linspace(0,len(stream_data),fs)
#Modulacion
#FSK
signal_fsk = FSK(stream_data, tb, fr1, fr2)
signal0_fsk = FSK(data0, tb, fr1, fr2)
signal1_fsk = FSK(data1, tb, fr1, fr2)
#ASK
#signal_ask = ASK(stream_data, tb, fr1, a1, a2)

#Direcciones de salida
#outputFile1 = "../Resources/Audio/Created/sample_ask.wav"
outputFile2 = "../Resources/Audio/Created/sample_fsk.wav"

#Escritura de archivos
#writeAudio(outputFile1, np.asarray(signal_ask), fs)
writeAudio(outputFile2, np.asarray(signal_fsk), fs)

"""plt.subplot(3,1,1)
plt.plot(signal0_fsk)
plt.subplot(3,1,2)
plt.plot(signal1_fsk)
plt.subplot(3,1,3 )
plt.plot(signal_fsk)
plt.show()"""

#---------------------------------------------------

print("Se creo el archivo")
input("Presionar boton...")

#---------------------------------------------------

data_img, fs = readAudio(outputFile2)
data_img_demod = correlation(signal_fsk, fr1, fr2, fs, len(signal_fsk), a1, T)

