from scipy.io import wavfile

def writeAudio(fileDir, data, frameRate):
    wavfile.write(fileDir, frameRate, data)
