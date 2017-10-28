import numpy as np
import matplotlib.pyplot as plt
from Source.Modulation.Digital import FSK
from Source.Modulation.Digital import ASK
from Source.IO.ReadImage import readImage
from Source.IO.ReadImage import readImageBN
from Source.IO.WriteAudio import writeAudio
from Source.Tools.intToBin import intToBin
from Source.Tools.ArrayToSignal import setBitRate
from Source.Modulation.Correlation import correlation
from Source.Modulation.Digital import demodBank


#Lectura de imagen en frames
img = readImageBN("../Resources/Sample Images/testIMG_1x2.jpg")
#Transformación de frames a su representación en bits
img_bin = intToBin(img, 8)
#
#stream_data = img_bin.ravel()#stream de datos
stream_data = [0,1,0,1,1,1,0]
fs = 44100  #frecuencia de muestreo
T = 1 #tiempo de bit
f1 = 3000 #frecuencia
f2 = 4000
tb = setBitRate(T, fs)
t = np.linspace(0,len(stream_data),fs)
amp = 10
data0=[0]
data1=[1]

#Modulacion FSK
signal0_fsk = FSK(data0, t, f1, f2)
signal1_fsk = FSK(data1, t, f1, f2)
data_fsk = FSK(stream_data, t, f1, f2)

#Graficos FSK

plt.subplot(3,1,1)
plt.plot(signal0_fsk)
plt.subplot(3,1,2)
plt.plot(signal1_fsk)
plt.subplot(3,1,3 )
plt.plot(data_fsk)
plt.show()

#Modulacion ASK
#signal0_ask = ASK(data0, t, fr, amp)
#signal1_ask = ASK(data1, t, fr, amp)
#data_ask = ASK(stream_data, t, fr, amp)

#Graficos ASK
"""
plt.subplot(3,1,1)
plt.plot(signal0_ask)
plt.subplot(3,1,2)
plt.plot(signal1_ask)
plt.subplot(3,1,3 )
plt.plot(data_ask)
plt.show()
"""
#Correlacion
data_demod = correlation(data_fsk, f1, f2, fs,len(stream_data), amp)
print(data_demod)
"""
plt.subplot(2,1,1)
plt.plot(stream_data)
plt.subplot(2,1,2)
plt.plot(data_demod)
plt.show()
"""