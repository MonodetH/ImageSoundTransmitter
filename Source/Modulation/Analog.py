from Source.Tools.SignalFactory import *
from Source.Filter.Butterworth import *
from Source.Tools.FFT import *

# Modulacion AM a una frecuencia en hertz targetFreqHZ
def amMod(data,frameRate,targetFreqHz):
    time = len(data)/frameRate
    portadora = cosFactory(targetFreqHz,frameRate,time)
    mod = data * portadora
    return mod

def amDemod(data,frameRate,targetFreqHz):
    time = len(data)/frameRate
    portadora = cosFactory(targetFreqHz,frameRate,time)
    demod = data * portadora

    demod = butterPasabajo(demod,targetFreqHz/2,frameRate,8)

    return demod

def fmMod(data, frameRate, targetFreqHz):
    freq = targetFreqHz + data
    ifreq = np.cumsum(freq) * (1 / float(frameRate))
    mod = np.cos(2 * np.pi * ifreq)
    return mod