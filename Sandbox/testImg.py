from Source.IO.ReadImage import readImage
from Source.IO.ReadImage import readImageBN
from Source.Tools.intToBin import intToBin
from Source.Tools.ArrayToSignal import arrayToSignal
from Source.IO.WriteAudio import writeAudio
from Source.Modulation.Analog import amMod
from Source.Plot.PlotSignal import plotSignal
import numpy as np
from time import sleep

#R, G, B = readImage("../Resources/Sample Images/sample1_l.jpg")
img = readImageBN("../Resources/Sample Images/testIMG.jpg")
#img_bin = intToBin(img, 8)
img_bin = [[1, 0, 1, 0, 1, 0, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0]]
img_bin = np.asarray(img_bin)


img_signal, frameRate = arrayToSignal(img_bin, 4, 44100)

am_imgSignal = amMod(img_signal, frameRate, 440.0)
writeAudio("../Resources/Audio/Created/testImg.wav", am_imgSignal, frameRate)

#R_bin = intToBin(R, 8)  #representacion en 8 bits
#G_bin = intToBin(G, 8)  #representacion en 8 bits
#B_bin = intToBin(B, 8)  #representacion en 8 bits

#test
"""for i in range(len(img_bin)):
    print(img[0][i])
    print(img_bin[i])
    sleep(2)"""