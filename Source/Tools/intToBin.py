import numpy as np

def intToBin(data, nbits):
    data = data.flatten()
    data_bin = []

    for elem in data:
        data_bin.append(list(np.binary_repr(elem, nbits)))

    return np.asarray(data_bin, np.int16)

def binToInt(data, shape):
    a = np.array(data)
    b = np.packbits(a, axis=-1)
    r = np.reshape(b, shape)
    return r
