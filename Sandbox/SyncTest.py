import pyaudio

from matplotlib import pyplot as plt

from Source.IO.Sync import *
import numpy as np
from scipy import signal

CHUNKSIZE = int(44100//0.25)  # fixed chunk size
sync = createSyncSignal()
success = createSuccessSignal()
error = createErrorSignal()

# initialize portaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=CHUNKSIZE)

print("Escuchando señal")

#####
# Ahora abrir un audio llamado syncSignal, successSignal o errorSignal
#####

while(True):
    data = stream.read(CHUNKSIZE)
    numpydata = np.fromstring(data, dtype=np.int16)

    signal= findSyncSignals(numpydata, sync, success, error)
    if(signal == 0):
        print("Sync encontrado!")
        break
    if (signal == 1):
        print("Success encontrado!")
        break
    if (signal == 2):
        print("Error encontrado!")
        break


# close stream
stream.stop_stream()
stream.close()
p.terminate()


# sig = numpy.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
# sig_noise = sig + numpy.random.randn(len(sig))
# corr = signal.correlate(sig_noise, numpy.ones(128), mode='same')
#
# plt.plot(corr)
# plt.show()
#
#
# sync = createSyncSignal()
# sig_noise = sync + numpy.random.randn(len(sync))
# corr = signal.correlate(numpy.append(numpy.append(sync,sig_noise),sync), sync, mode='same')
#
# plt.plot(corr)
# plt.show()

# error = createErrorSignal()
# success = createSuccessSignal()
#
# writeAudio("../Resources/Audio/Created/syncSignal.wav",sync,44100)
# writeAudio("../Resources/Audio/Created/errorSignal.wav",error,44100)
# writeAudio("../Resources/Audio/Created/successSignal.wav",success,44100)
#
# spectrogram(sync,44100)
# spectrogram(error,44100)
# spectrogram(success,44100)

