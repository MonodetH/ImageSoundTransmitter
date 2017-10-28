from Source.Tools.FFT import *
from Source.Plot.PlotFFT import *
from Source.Plot.Spectrogram import *
from Source.IO.ReadAudio import *


data,frameRate = readAudio("../Resources/Audio/ask-snr=2.wav")

plotFFT(data,frameRate)

bandwidth = findBandWidth(data,frameRate,0.02 )
