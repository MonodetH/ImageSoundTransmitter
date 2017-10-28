import pyaudio
import wave

def recordAudio(direccion, duracion):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    frames = []

    #la condicion señal de partida se hará cero si la escucha

    senalpartida = 1
    j = 0
    #el j<10 es para hacer solo 10 pruebas de señal de partida
    while(senalpartida and j<10):
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        print("Grabando")
        for i in range(0, int(RATE / CHUNK * duracion)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(direccion, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("fin prueba " + str(j))

        #acá hay que analizar si el sonido grabado contiene la señal de sincronización

        j=j+1

        input("Pulsa enter para continuar...")

    print("se ha escuchado señal de partida")

    #for i in range(0, int(RATE / CHUNK * duracion)):
    #    data = stream.read(CHUNK)
    #    frames.append(data)

    #print("Terminado")

    #stream.stop_stream()
    #stream.close()
    #p.terminate()

    #wf = wave.open(direccion, 'wb')
    #wf.setnchannels(CHANNELS)
    #wf.setsampwidth(p.get_sample_size(FORMAT))
    #wf.setframerate(RATE)
    #wf.writeframes(b''.join(frames))
    #wf.close()