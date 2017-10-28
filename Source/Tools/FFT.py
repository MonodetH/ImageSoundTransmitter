import numpy as np
from scipy.fftpack import fft, fftfreq

from Source.Plot.PlotFFT import *

import matplotlib.pyplot as plt

## Codigo basado en respuesta de stackoverflow
# http://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python
def findMaxFreq(data,frameRate):

    ## Obtener los datos de la transformada y sus frecuencias asociadas
    datafft = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(datafft))

    # Buscar el indice del valor max
    max = np.argmax(np.abs(datafft))

    # Determinar el indice de la frecuencia maxima
    freq = freqs[max]

    # normalizar la frecuencia a hertz
    hz = abs(freq * frameRate)

    return hz

# El valor del threshold (umbral) es un flotante entre 0 y 1 y representa el porcentaje del peso de la frecuencia predominante
def findBandWidth(data,frameRate,threshold=0.05):
    ## Obtener los datos de la transformada y sus frecuencias asociadas
    datafft = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(datafft))

    # Determinar el mayor peso dentro de la fft
    max = datafft[np.argmax(np.abs(datafft))]

    # Determinar el indice de la mayor frecuencia no nula
    for i in range(len(np.abs(datafft))//2,0,-1):
        if datafft[i] > max*threshold:
            freq = i
            break

    # Determinar el indice de la frecuencia maxima
    freq = freqs[freq]

    # normalizar la frecuencia a hertz
    hz = abs(freq * frameRate)

    return hz
