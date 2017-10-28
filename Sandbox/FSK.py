import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from Source.Modulation.Analog import *

v=[0,1,0,1,0,1,0,0,0,1] #señal binaria
cantMuestra = 100 #numero de muestras por cada dato de la señal
vx = []
fsk = []
for i in range (0,len(v)):
    t = np.ones(cantMuestra) #vector de unos
    x = t*v[i]
    vx = np.concatenate((vx,x))#vector binario con la cantidad de muestras deseadas
plt.subplot(4,1,1)
plt.ylim(0, 1.1);#para que se vea bien la señal
plt.plot(vx)
#print(len(vx))
cantMuestra2 = len(vx)
t = np.linspace(0,10,cantMuestra2)# duracion de 10 segundos con numero de muestras cantMuestra
f1 = 5 #frecuencia del primer coseno

plt.subplot(4,1,2)
w1 = 2*pi*f1*t #frecuencia del coseno
y1 = np.cos(w1)
plt.plot(t,y1)
plt.subplot(4,1,3)
f2 = 10 #frecuencia del segundo coseno
w2 = 2*pi*f2*t
y2 = np.cos(w2)
plt.plot(t,y2)
plt.subplot(4,1,4)

#

for k in range(len(vx)):

    if vx[k] == 0:
        cero = np.array([y1[k]])

        fsk = np.concatenate((fsk, cero))
    else:
        uno = np.array([y2[k]])

        fsk = np.concatenate((fsk,uno))
plt.plot(t,fsk)
plt.show()