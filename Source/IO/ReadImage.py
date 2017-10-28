import numpy as np
from scipy import ndimage

import matplotlib.pyplot as plt

def readImage(fileDir):
    img = ndimage.imread(fileDir)   #Matriz M, donde M[i, j] = [R, G, B]
    R = []
    G = []
    B = []
    for i in img:
        Rr = []
        Gr = []
        Br = []
        for j in i:
            Rr.append(j[0])
            Gr.append(j[1])
            Br.append(j[2])
        R.append(Rr)
        G.append(Gr)
        B.append(Br)

    npR = np.asarray(R, np.int16)
    npG = np.asarray(G, np.int16)
    npB = np.asarray(B, np.int16)
    return npR, npG, npB

def readImageBN(fileDir):
    img = ndimage.imread(fileDir, flatten=True, mode="L")
    return np.asarray(img, np.int16)
