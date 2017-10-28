import numpy as np
from scipy import signal
from Source.Modulation.Analog import fmMod
from Source.Plot.PlotSignal import plotSignal

## CREAR SEÑALES
def createSyncSignal(frameRate = 44100, carrier = 8000):
    duration = 0.25
    #base = np.linspace(0, duration, int(frameRate * duration))
    #data = (400*np.sin(24*base)+150*np.cos(121*base)+700*np.sin(521*base)+500*np.cos(1132*base)+150)
    freq = np.linspace(10000, 15000, int(frameRate * duration/2))
    freq = np.append(freq,freq[::-1])
    ifreq = np.cumsum(freq) * (1 / frameRate)
    data = np.cos(2 * np.pi * ifreq)

    #data = fmMod(data, frameRate, carrier)
    return data


def createErrorSignal(frameRate = 44100, carrier = 8000):
    duration = 0.25
    base = np.linspace(0, duration, int(frameRate * duration))
    data = 20*(-1921 * base ** 3 -192 * base ** 2) + 90*np.sin(563 * base) + 1600
    data = fmMod(data, frameRate, carrier)
    return data


def createSuccessSignal(frameRate = 44100, carrier=8000):
    duration = 0.25
    base = np.linspace(0, duration, int(frameRate * duration))
    data = 30*(1681 * base ** 3 + 168 * base ** 2) + 150*np.sin(642 * base)
    data = fmMod(data, frameRate, carrier)
    return data


## ENCONTRAR SEÑALES
def findSyncSignals(data, sync=None, success=None, error=None):
    if sync is None:
        sync = createSyncSignal()
    if error is None:
        error = createErrorSignal()
    if success is None:
        success = createSuccessSignal()

    ratios = []
    corr = np.absolute(signal.fftconvolve(data, sync[::-1], mode='valid'))
    corr = corr / max(corr)
    syncRatio = max(corr)/np.mean(corr)
    ratios.append(syncRatio)

    corr = np.absolute(signal.fftconvolve(data, success[::-1], mode='valid'))
    corr = corr / max(corr)
    successRatio = max(corr) / np.mean(corr)
    ratios.append(successRatio)

    corr = np.absolute(signal.fftconvolve(data, error[::-1], mode='valid'))
    corr = corr / max(corr)
    errorRatio = max(corr) / np.mean(corr)
    ratios.append(errorRatio)

    # print(ratios)

    maxIndex = np.argmax(np.array(ratios))
    maxValue = ratios[maxIndex]
    if maxValue > 18:
        return maxIndex
    return -1

def findResponseSignals(data, success=None, error=None):
    if error is None:
        error = createErrorSignal()
    if success is None:
        success = createSuccessSignal()

    ratios = []

    corr = np.absolute(signal.fftconvolve(data, success[::-1], mode='valid'))
    corr = corr / max(corr)
    successRatio = max(corr) / np.mean(corr)
    ratios.append(successRatio)

    corr = np.absolute(signal.fftconvolve(data, error[::-1], mode='valid'))
    corr = corr / max(corr)
    errorRatio = max(corr) / np.mean(corr)
    ratios.append(errorRatio)

    # print(ratios)

    maxIndex = np.argmax(np.array(ratios))
    maxValue = ratios[maxIndex]
    if maxValue > 18:
        return maxIndex
    return -1

def findSyncSignal(data, sync=None):
    if sync is None:
        sync = createSyncSignal()
    corr = np.absolute(signal.fftconvolve(data, sync[::-1], mode='valid'))
    corr = corr / max(corr)
    maxValue = max(corr)
    avgValue = np.mean(corr)
    if (maxValue/avgValue > 20):
         return np.argmax(corr)
    return None

def findErrorSignal(data, sync=None):
    if sync is None:
        sync = createErrorSignal()
    corr = np.absolute(signal.fftconvolve(data, sync[::-1], mode='valid'))
    corr = corr / max(corr)
    maxValue = max(corr)
    avgValue = np.mean(corr)
    if (maxValue / avgValue > 20):
        return True
    return False

def findSuccessSignal(data, sync=None):
    if sync is None:
        sync = createSuccessSignal()
    corr = np.absolute(signal.fftconvolve(data, sync[::-1], mode='valid'))
    corr = corr / max(corr)
    maxValue = max(corr)
    avgValue = np.mean(corr)
    if (maxValue / avgValue > 20):
        return True
    return False

