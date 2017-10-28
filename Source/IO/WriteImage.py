import numpy as np
from Source.Tools.intToBin import binToInt
import scipy

def writeImageBN(data, dim, fileName):
    imgMatrix = np.reshape(data, (-1, 8))
    imgInt = binToInt(data, dim)
    scipy.misc.imsave(fileName, imgInt)