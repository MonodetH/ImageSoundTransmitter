from Source.Modulation.Digital import MFSK
from Source.IO.Sync import createSyncSignal
import pyaudio
import numpy as np

sync = createSyncSignal()
datos = np.append(sync, MFSK([1,0,1,0],16,5000,9000))

CHUNK = 1024
FRAMERATE = 44100


p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=FRAMERATE,
                output=True)


streamData = datos.astype(np.float32).tostring()

stream.write(streamData)

stream.stop_stream()
stream.close()

p.terminate()

