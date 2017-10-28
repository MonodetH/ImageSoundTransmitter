from Source.Tools.SignalFactory import cosFactory
import numpy as np


def ASK(data, tb, fr, a0, a1):
    tx = []

    sign0 = a0*np.cos(2*np.pi*fr*tb)
    sign1 = a1*np.cos(2*np.pi*fr*tb)

    for bit in data:
        if bit == 1:
            tx.extend(sign1)
        else:
            tx.extend(sign0)

    return tx


def FSK(data, tb, f0, f1):
    tx = []

    sign0 = np.cos(2*np.pi*f0*tb)
    sign1 = np.cos(2*np.pi*f1*tb)

    for bit in data:
        if bit == 1:
            tx.extend(sign1)
        else:
            tx.extend(sign0)

    return tx


def MFSK(data, bitsPerSimbol, minHz, maxHz, frameRate=44100, baudRate=2):
    nSimbols = 2 ** bitsPerSimbol
    freqs = []
    for i in range(nSimbols+1):
        freq = minHz + i * (maxHz - minHz) / nSimbols
        signal = cosFactory(int(freq), frameRate, 1.0 / baudRate)
        freqs.append(signal)

    simbolData = []
    signal = []

    # Mapear datos a simbolos
    padding = int(len(data)%bitsPerSimbol)

    if padding>0:
        print("Warning: Datos no calzan con el numero de simbolos, hay un corrimiento de",bitsPerSimbol-padding,"bits")
        out = 0
        for bit in data[:padding]:
            out = (out << 1) | bit
        simbolData.append(out)

    for i in range(padding,len(data),bitsPerSimbol):
        out = 0
        for bit in data[i:i+bitsPerSimbol]:
            out = (out << 1) | bit
        simbolData.append(out)

    for simbol in simbolData:
        if simbol<0 or simbol>=nSimbols:
            break
        signal.extend(freqs[simbol])

    return np.array(signal)



def demodBank(data, tb, f0, f1, a0, a1):
    b = []

    sign0 = a0*np.cos(2*np.pi*f0*tb)
    sign1= a1*np.cos(2*np.pi*f1*tb)

    v0 = np.correlate(data, sign0, mode="same")
    v1 = np.correlate(data, sign1, mode="same")

    for i in range(0, len(data)):
        if v0[i] > v1[i]:
            b.append(0)
        else:
            b.append(1)

    return b