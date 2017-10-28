from Source.IO.Transmission import *
from Source.IO.WriteImage import *


largoTrama = 7*8
bitsPorSimbolo = 4
baudRate = 5

#normas = receiveNorm(bitsPorSimbolo)

normas=None

#sendResponse(True)

data = receiveData(largoTrama,bitsPorSimbolo,baudRate,norm=normas)

writeImageBN(data,(7,7),"../Resources/Sample Images/testIMG7x7.jpg")

print(data)

