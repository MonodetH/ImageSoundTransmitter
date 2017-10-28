from Source.IO.Sync import *
from Source.Modulation.Correlation import correlateBank
from Source.Tools.SignalFactory import cosFactory
from Source.Modulation.Digital import MFSK

import numpy as np
from scipy import signal
import pyaudio
from matplotlib import pyplot as plt


datos = MFSK([1,0,1,0],2,5000,9000)
corr = correlateBank(datos,2,5000,8000)

plt.subplot(2,1,1)
plt.plot(corr[0])
plt.subplot(2,1,2)
plt.plot(corr[1])
plt.show()


