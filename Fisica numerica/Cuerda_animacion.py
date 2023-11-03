#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:39:14 2023

@author: diego
"""


import numpy as np 
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation

#Establecemos las constantes para el aluminio 
T=30
rho=1.1

L=100 #longitud total 
t_medicion=50 #Tiempo de observacion 
n_x=20 #Numero de puntos de la coordenada x
n_t=110 #Numero de puntos de la coordenada y
 
delta_x= L/(n_x) #calculamos los pasos 
delta_t= t_medicion / (n_t)
c=np.sqrt(T/rho)
c_p=delta_x/delta_t

print(c/c_p)

#Creamos la matriz donde guardaremos nuestros valores de la cuerda
y=np.zeros((n_t+1,n_x+1))
x=np.linspace(0,L,n_x+1)
#Establecemos las condiciones de frontera, que estan en primera y ultima columna de la matriz:
for i in range(n_t+1):
    y[i][0]=0
    y[i][n_x]=0
#Establecemos la Codicion inicial:
for i in range(len(x)):
    if x[i]<=0.8*L:
        y[0][i]=1.25*x[i]/L
    if x[i]>0.8*L:
        y[0][i]=5-(5*x[i])/L
        

for j in range(0,n_t): #Recorremos todas las filas 
    for i in range(1,n_x): #Por cada fila recorremos las columnas y asi poder recorrer toda la matriz 
        y[j+1][i] = 2*y[j][i]-y[j-1][i]+((c/c_p)**2)*(y[j][i+1] + y[j][i-1]-2*y[j][i])


#________________________________________________________________________________________________________________________
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-10, 10)  
plt.xlabel('Posicion [m]')
plt.ylabel('Altura [m]')
plt.title('Simulacion de la onda en una cuerda')


line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    y_i = y[i]
    line.set_data(x, y_i)
    return line,


ani = FuncAnimation(fig, animate, frames=n_t, init_func=init, blit=True)

plt.show()
