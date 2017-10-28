import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def spectrogram(data,framerate, image=None):

    f, t, Sxx = signal.spectrogram(data, framerate, nfft=512)
    plt.pcolormesh(t, f, Sxx)
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [seg]')
    plt.colorbar()
    if image != None:
        plt.savefig("../Resources/Images/" + image + ".png")
    plt.show()
