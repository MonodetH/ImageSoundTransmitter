import numpy as np
import matplotlib.pyplot as plt

def cosFactory(freq, frameRate, duration):
    base = np.linspace(0, duration, frameRate * duration)
    data = np.cos(2 * np.pi * freq * base)
    return data

def sinFactory(freq, frameRate, duration):
    base = np.linspace(0, duration, frameRate * duration)
    data = np.sin(2 * np.pi * freq * base)
    return data

def cosCreciente(frameRate, duration):
    base = np.linspace(0, duration, frameRate * duration)
    freq = np.linspace(20, 20000, frameRate * duration)
    ifreq = np.cumsum(freq)*(1/frameRate)
    data = np.cos(2 * np.pi * ifreq)
    return data


