from Source.Modulation.Digital import FSK
from Source.Tools.SignalFactory import cosFactory
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal


def window_rms(a, window_size):
  a2 = np.power(a,2)
  window = np.ones(window_size)/float(window_size)
  return np.sqrt(np.convolve(a2, window, 'valid'))

def correlation (signal_mod,f1, f2,fs,data_len, amp, T):
    Vx = []
    #t = np.linspace(0, data_len, fs)
    tb = np.linspace(0, 1, fs * T)
    data0 = [0]
    data1 = [1]
    signal0_fsk = FSK(data0, tb, f1, f2)
    signal1_fsk = FSK(data1, tb, f1, f2)
    correlate_data0 = np.correlate(signal0_fsk, signal_mod, mode='same')
    correlate_data1 = np.correlate(signal1_fsk, signal_mod, mode='same')
    """
    correlate_data0 = correlate_data0 * correlate_data0
    correlate_data1 = correlate_data1 * correlate_data1
    correlate_data0 = np.abs(correlate_data0)
    correlate_data1 = np.abs(correlate_data1)
    correlate_data0 = signal.medfilt(correlate_data0)
    correlate_data1 = signal.medfilt(correlate_data1)
    """
    correlate_data0 = window_rms(correlate_data0,10000)
    correlate_data1 = window_rms(correlate_data1,10000)
    plt.plot(correlate_data0)
    plt.plot(correlate_data1)
    plt.show()
    #print(len(signal_mod))
    aux = 0
    for i in range(len(signal_mod)):

        if aux == fs*T/2:
            aux = -(fs*T/2)
            t0 = correlate_data0[i]
            t1 = correlate_data1[i]
            if t0 >= t1:
                Vx.extend(data0)
            else:
                Vx.extend(data1)
        aux = aux+1
    b = Vx[::-1]
    return b


def correlate(signalBase, signalTarget):
    if signalTarget is None or signalBase is None:
        return None

    corr = np.absolute(signal.fftconvolve(signalBase, signalTarget[::-1], mode='valid'))
    maxValue = max(corr)
    corr = corr / maxValue
    return corr


def correlateBank(signalBase, bitsPerSimbol, minHz, maxHz, frameRate=44100, baudRate=2):
    nSimbols = 2**bitsPerSimbol
    correlations = []

    # Correlacionar
    for i in range(nSimbols):
        freq = minHz + i * (maxHz - minHz) / nSimbols
        signalTarget = cosFactory(int(freq), frameRate, 0.25/baudRate)
        corr = np.absolute(signal.fftconvolve(signalBase, signalTarget[::-1], mode='valid'))
        correlations.append(corr)

    return correlations

def correlationToData(correlation, bitsPerSimbol, baudRate, norm=None,frameRate = 44100):
    framesPerSimbol = frameRate/float(baudRate)
    nSimbols = 2 ** bitsPerSimbol
    data = []
    keyFrames = np.arange(framesPerSimbol/2,len(correlation[0]),framesPerSimbol)

    # Normalizar
    if norm is None:
        maxValue = 0
        for i in range(nSimbols):
            maxValue = max([maxValue, max(correlation[i])])
        for i in range(nSimbols):
            correlation[i] = window_rms(correlation[i] / maxValue, 200)
    else:
        for i in range(nSimbols):
            correlation[i] = window_rms(correlation[i] / norm[i], 200)


    for i in range(len(correlation)):
        plt.plot(correlation[i])
    plt.show()

    for i in keyFrames:
        values = []
        for j in range(nSimbols):
            corrValue = correlation[j][int(i)]
            values.append(corrValue)
        simbol = np.argmax(values)
        # convertir simbolo a bit
        bits = [1 if digit=='1' else 0 for digit in bin(simbol)[2:]]
        if len(bits) < bitsPerSimbol:
            data.extend([0]*(bitsPerSimbol-len(bits)))
        data.extend(bits)
    return data

def getNormas(correlationData,bitsPerSimbol):
    nSimbols = 2 ** bitsPerSimbol
    normas = []

    for i in range(len(correlationData)):
        normas.append(max(correlationData[i]))

    return normas