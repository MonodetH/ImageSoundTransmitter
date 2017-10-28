import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import correlate

from Source.Tools.ArrayToSignal import setBitRate
from Source.Modulation.Digital import FSK
from Source.Modulation.Digital import ASK
from Source.IO.WriteAudio import writeAudio
from Source.IO.ReadImage import readImageBN
from Source.Tools.intToBin import intToBin
from Source.Tools.ArrayToSignal import arrayToSignal

data = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]

#Lectura de imagen en frames
img = readImageBN("../Resources/Sample Images/testIMG_1x2.jpg")
#Transformación de frames a su representación en bits
img_bin = intToBin(img, 8)
#Paso de bits a señal
img_signal, frameRate = arrayToSignal(img_bin, 4, 44100)
a = img_bin.ravel()
print(a)
Vx =[]
data0=[0]
data1=[1]
fs = 100  #frecuencia de muestreo
T = 1 #tiempo de bit
fr = 50 #frecuencia
tb = setBitRate(T, fs)
t = np.linspace(0,len(a),fs)

signal0_fsk = FSK(data0, tb, fr)
signal1_fsk = FSK(data1, tb, fr)
data_fsk = FSK(a, tb, fr)

correlate_data0 = np.correlate(signal0_fsk, data_fsk, mode='same')
correlate_data1 = np.correlate(signal1_fsk, data_fsk, mode='same')

for i in range(len(data_fsk)):
        #print(i/fs)

        t0 = correlate_data0[int(i)]      #
        t1 = correlate_data1[int(i)]
        #print("t0=",t0)
       # print("t1=",t1)
        if(t0 == np.amax(correlate_data0)):
            #print("i= ",i)
            Vx.extend(data0)
        if(t1 == np.amax(correlate_data1)):
            #print("i= ", i)
            Vx.extend(data1)


print(np.amax(correlate_data0))
print(len(data_fsk))
print(np.amax(correlate_data1))

b = Vx[::-1]
print(b)

"""
plt.subplot(3,1,1)
plt.plot(signal0_fsk)
plt.subplot(3,1,2)
plt.plot(signal1_fsk)
plt.subplot(3,1,3)
plt.plot(data_fsk)
"""
#a= Stream(img_bin)
#print(a)
#plt.imshow(img_bin,cmap="gray")
#plt.show()

#writeAudio("../Resources/Audio/Created/data_fsk.wav", np.array(data_fsk), fs)
#writeAudio("../Resources/Audio/Created/sample_fsk_data_1.wav", np.asarray(signal1_fsk), fs)