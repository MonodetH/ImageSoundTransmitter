import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from Source.Modulation.Analog import *
#a = np.linspace(-6*pi,6*pi,100)
#coseno = cos(a)
v=[0,1,0,1,0,1,0,0,0,1] #señal binaria
cantMuestra = 100 #numero de muestras por cada dato de la señal
vx = []
for i in range (0,10):
    t = np.ones(cantMuestra) #vector de unos
    x = t*v[i]
    vx = np.concatenate((vx,x))#vector binario con la cantidad de muestras deseadas
plt.subplot(3,1,1)
plt.plot(vx)
#print(len(vx))
cantMuestra2 = len(vx)
t = np.linspace(0,10,cantMuestra2)# duracion de 10 segundos con numero de muestras cantMuestra
f = 5 #frecuencia

plt.subplot(3,1,2)
w = 2*pi*f*t #frecuencia del coseno
y1 = cos(w)
plt.plot(t,y1)
plt.subplot(3,1,3)
mod = vx*y1 #multiplicacion de la señal binaria por el coseno
plt.plot(t,mod)
plt.show()