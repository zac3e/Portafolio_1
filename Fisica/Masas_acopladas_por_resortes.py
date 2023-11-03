#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:54:03 2023

@author: diego
"""

import matplotlib.pyplot as plt
import numpy as np


# Definición de constantes
N=1000           # Número de pasos
tau=150  # Tiempo en segundos de la simulación
h=tau/float(N-1)   # Paso del tiempo 
k=1.0 #Cosntante de acoplamiento
k_1=2.0
m=60.0

#Condiciones iniciales de el movimiento lineal 
#__________________________________________________________________________________
x_1=5.0
x_2=0.0  
v_x1=0.0
v_x2=0.0 

#Condiciones iniciales de el movimiento no lineal 
#_________________________________________________________________
x_1nl=5.0
x_2nl=0.0  
v_x1nl=0.0
v_x2nl=0.0  

#________________________________________________________________________________________________
# Generamos un arreglo de Nx4 para almacenar posición y velocidad para los dos casos 

y=np.zeros([N,4])
ynl=np.zeros([N,4])

# tomamos los valores del estado inicial para caso lineal y no lineal
y[0,0]=x_1
y[0,1]=v_x2
y[0,2]=x_2
y[0,3]=v_x2

ynl[0,0]=x_1nl
ynl[0,1]=v_x2nl
ynl[0,2]=x_2nl
ynl[0,3]=v_x2nl

# Generamos tiempos igualmente espaciados
tiempo=np.linspace(0,tau,N)

# Definimos nuestra ecuación diferencial en caso lineal y no lineal 
#___________________________________________________________________________________________________________________
def EDO(estado,tiempo):
        f0=estado[1]
        f1=(1/m)* (-k_1*estado[0]+k*(estado[2]-estado[0]))
        f2=estado[3]
        f3=(1/m)*(-k_1*estado[2]-k*(estado[2]-estado[0]))
        return np.array([f0,f1,f2,f3])
    
def EDONL(estado,tiempo):
        f0=estado[1]
        f1=(1/m)*(-k_1*(estado[0]+(0.1)*(estado[0]**3))+k*((estado[2]-estado[0])+(0.1)*((estado[2]-estado[0])**3)))
        f2=estado[3]
        f3=(1/m)*(-k_1*(estado[0]+(0.1)*(estado[0]**3))-k*((estado[2]-estado[0])+(0.1)*((estado[2]-estado[0])**3)))
        return np.array([f0,f1,f2,f3]) 



# Método de Rk4 para  resolver numéricamente la EDO 
def rk4(y,t,h,f,N):
    k1=np.zeros(N); k2=np.zeros(N); k3=np.zeros(N); k4=np.zeros(N)
    k1 = h*f(y,t)                             
    k2 = h*f(y+k1/2.,t+h/2.)
    k3 = h*f(y+k2/2.,t+h/2.)
    k4 = h*f(y+k3,t+h)
    y=y+(k1+2*(k2+k3)+k4)/6.
    return y  

#Usamos el for para calcular todas los elementos de Y en casp lineal y no lineal 
#____________________________________________________________________________________________
for j in range(N-1):
    y[j+1]=rk4(y[j],tiempo[j],h,EDO,[N,4])
    ynl[j+1]=rk4(ynl[j],tiempo[j],h,EDONL,[N,4])
    
#_______________________________________________________________________________________________________-
x_1datos=[y[j,0] for j in range(N)]
v_x1datos=[y[j,1] for j in range(N)]
x_2datos=[y[j,2] for j in range(N)]
v_x2datos=[y[j,3] for j in range(N)]

x_1nldatos=[ynl[j,0] for j in range(N)]
v_xnl1datos=[ynl[j,1] for j in range(N)]
x_2nldatos=[ynl[j,2] for j in range(N)]
v_x2nldatos=[ynl[j,3] for j in range(N)]

#________________________________________________________________________________________________________
fig, ax = plt.subplots(1, 2) 
fig.suptitle('Movimiento lineal vs movimiento no lineal')
#_________________________________________________________________________
ax[0].plot(tiempo, x_1datos, color="red", label="Lineal")
ax[0].plot(tiempo, x_1nldatos, color="blue",label="No Lineal")
ax[0].legend(["Lineal", "No lineal"], loc="upper left") #legendas
ax[0].set_title('Movimiento de masa 1')
ax[0].set_xlabel('Tiempo')
ax[0].set_ylabel('Posicion')
#________________________________________________________________________
ax[1].plot(tiempo, x_2datos, color="red",label="Lineal")
ax[1].plot(tiempo, x_2nldatos, color="blue",label="No Lineal")
ax[1].legend(["Lineal", "No lineal"], loc="upper left") #legendas
ax[1].set_title('Movimiento de masa 2')
ax[1].set_xlabel('Tiempo')
ax[1].set_ylabel('Posicion')

#_______________________________________________________________________

fig.tight_layout() #Se acomoden automaticamente
plt.show()
