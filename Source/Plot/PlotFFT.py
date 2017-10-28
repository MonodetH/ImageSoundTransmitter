import numpy as np
from scipy.fftpack import fft, fftfreq

import matplotlib.pyplot as plt

def plotFFT(data,frameRate, title, image=None):
    n = len(data)
    data_fft = fft(data)/n

    #Se configura eje de Frecuencias
    mid = int(n/2)
    data_fft = data_fft[range(mid)]

    k = np.arange(n)
    T = n/float(frameRate)
    freq = k/T
    freq = freq[range(mid)]

    #Se grafica FFT
    plt.plot(freq, abs(data_fft), '-')
    plt.title(title)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("|F(w)|")

    if (image!=None):
        plt.savefig("../Resources/Images/"+image+".png")
    plt.show()
    return data_fft

def plotFFTLog(data,frameRate, title, image=None):
    n = len(data)
    data_fft = fft(data)/n

    #Se configura eje de Frecuencias
    mid = int(n/2)
    data_fft = data_fft[range(mid)]

    k = np.arange(n)
    T = n/frameRate
    freq = k/T
    freq = freq[range(mid)]

    #Se grafica FFT
    plt.plot(freq, abs(data_fft), '-')
    plt.yscale('log')
    plt.title(title)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Log(F(w))")

    if (image!=None):
        plt.savefig("../Resources/Images/"+image+".png")
    plt.show()
    return data_fft