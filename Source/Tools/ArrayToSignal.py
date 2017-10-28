import numpy as np

def arrayToSignal(data, bitRate, frameRate):
    data = data.flatten()
    mpb = frameRate/bitRate #Cantidad de muestras por bit
    carryBit = 0
    sal = []
    amp = 1
    for i in range(len(data)):
        muestras = int(mpb)
        carryBit += mpb % 1
        if carryBit >= 1:
            muestras += 1
            carryBit -= 1

        sal.extend([amp*data[i]]*muestras)

    sal = np.asarray(sal)
    return sal, frameRate

def setBitRate(T, fs):
    tb = np.linspace(0, T, fs)
    return tb
