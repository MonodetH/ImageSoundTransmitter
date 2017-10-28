import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from Source.Modulation.Analog import *
from Source.Tools.SignalFactory import *
from Source.Plot.PlotFFT import *

# constantes
fr = 44100
duration = 0.1
origFreq = 500
objFreq = 1273
# Modulacion
vx = cosFactory(origFreq,fr,duration)

cantMuestra2 = len(vx)
t = np.linspace(0,duration,cantMuestra2)# duracion de 1 segundo con numero de muestras cantMuestra

plt.subplot(3,1,1)
plt.plot(t,vx)


y1 = cosFactory(objFreq,fr,duration)
plt.subplot(3,1,2)
plt.plot(t,y1)


mod = amMod(vx,fr,objFreq)
plt.subplot(3,1,3)
plt.plot(t,mod)

plt.show()



# Demodulacion
plt.subplot(2,1,1)
plt.plot(t,mod)

demod = amDemod(mod,fr,objFreq)
plt.subplot(2,1,2)
plt.plot(t,demod)

plt.show()

#FFT

plotFFT(vx,fr)

plotFFT(mod,fr)

plotFFT(demod,fr)



