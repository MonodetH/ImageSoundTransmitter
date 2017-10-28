import numpy as np
import matplotlib.pyplot as plt
from Source.Plot.PlotFFT import plotFFT
from Source.Tools.ArrayToSignal import setBitRate
from Source.Modulation.Digital import FSK
from Source.Modulation.Digital import ASK
from Source.Modulation.Digital import demodBank
from Source.IO.WriteAudio import writeAudio

data = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1]
fs = 100      #frecuencia de muestreo
T = 1        #tiempo de bit
fr = 5          #frecuencia
amp = 1         #amplitud
tb = setBitRate(T, fs)
t = np.linspace(0, len(data)*T, fs)

#data_ask = ASK(data, tb, fr, amp)
data_fsk = FSK(data, tb, fr, amp)

#writeAudio("../Resources/Audio/Created/sample_fsk.wav", np.asarray(data_fsk), fs)

plt.subplot(2, 1, 1)
datax = []
#Proceso plot señal digital
for i in range (0,len(data)):
    t = np.ones(fs)
    x = t*data[i]
    datax.extend(x)
plt.ylim(0, 1.1)
plt.plot(datax)

t = np.linspace(0, len(data)*T, len(data_fsk))  #vector de tiempo

plt.subplot(2, 1, 2)
plt.plot(t, data_fsk)
plt.show()

data_demod = demodBank(data_fsk, tb, fr, amp)
print(data_demod)


#t = np.linspace(0, len(data)*T, len(data_original))
#plt.plot(t, data_original)
#plt.show()
