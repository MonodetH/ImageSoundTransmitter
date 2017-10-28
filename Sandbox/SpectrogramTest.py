from Source.Plot.Spectrogram import *
from Source.IO.ReadAudio import readAudio
from Source.IO.WriteAudio import writeAudio
import numpy as np


time = 100
frameRate = 44100
freq = 500
sample = np.linspace(0, time, frameRate * time)
data = np.sin(2 * np.pi * (freq+(sample)) * sample)

#Spectrogram(data,frameRate)

write()

data, frameRate =  read('../Resources/Audio/Created/sample.wav')
data, frameRate =  read('../Resources/Audio/ook.wav')

print(len(data), frameRate)

Spectrogram(data,frameRate)