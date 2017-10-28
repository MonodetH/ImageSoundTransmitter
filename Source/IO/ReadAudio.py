# coding=utf-8
import numpy as np
from scipy.io import wavfile

def readAudio(fileDir):
    #Se obtienen los datos del archivo .wav a través de la función read() del módulo wavfile de scipy
    frameRate, data = wavfile.read(fileDir)
    #Datos de la señal
    #sinData = np.sin(data)
    return data, frameRate
