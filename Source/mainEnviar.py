from Source.IO.Transmission import *
from Source.IO.ReadImage import *
from Source.Tools.intToBin import *
import time


data = readImageBN("../Resources/Sample Images/testIMG.jpg")
data = intToBin(data,8)
data = data.ravel()
print(data)
streamData = np.reshape(data,(-1,8*7))

bitsPerSimbol = 8
baudRate = 6

#sendSimbols(bitsPerSimbol)

#waitResponse()

for trama in streamData:
    sendData(data,bitsPerSimbol,baudRate)
    waitResponse()
    time.sleep(0.2)



