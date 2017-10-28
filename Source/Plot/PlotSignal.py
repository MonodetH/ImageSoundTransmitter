import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plotSignal(data, frameRate, image=None):
    mpl.rcParams['agg.path.chunksize'] = 10000

    n = len(data)
    plt.plot(np.arange(0,n/float(frameRate),1/float(frameRate)), data)

    plt.xlabel("Time [s]")
    plt.ylabel("Amplitud [dB]")
    if image != None:
        plt.savefig("../Resources/Images/" + image + ".png")
    plt.show()