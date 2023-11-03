#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:41:21 2023

@author: diego
"""

import matplotlib.pyplot as plt
import numpy as np
# Definición de constantes
N=1000           # Número de pasos
x_0=0.0           # Posición inicial
y_0=2.0
v_x0=18.0   
v_y0=18.0        # Velocidad inicial
tau=5   # Tiempo en segundos de la simulación
h=tau/float(N-1)   # Paso del tiempo 
m=7.26
C_d=0.5
C_di=0.75
rho=1.2
R=0.06
A=np.pi * R
g=9.8
#________________________________________________________________________________________________
# Generamos un arreglo de Nx4 para almacenar posición y velocidad
y=np.zeros([N,4])
yf=np.zeros([N,4])
yfi=np.zeros([N,4])
# tomamos los valores del estado inicial
y[0,0]=x_0
y[0,1]=v_x0
y[0,2]=y_0
y[0,3]=v_y0

yf[0,0]=x_0
yf[0,1]=v_x0
yf[0,2]=y_0
yf[0,3]=v_y0

yfi[0,0]=x_0
yfi[0,1]=v_x0
yfi[0,2]=y_0
yfi[0,3]=v_y0

# Generamos tiempos igualmente espaciados
tiempo=np.linspace(0,tau,N)

# Definimos nuestra ecuación diferencial sin friccion 

def EDO(estado,tiempo):
        f0=estado[1]
        f1=0
        f2=estado[3]
        f3=-g
        return np.array([f0,f1,f2,f3]) 
#Ecuacion para el calculo del sistema estable
def EDOf(estado,tiempo):
        f0=estado[1]
        f1=-(A/m)*rho*0.5*C_d*(estado[1]**2+estado[3]**2)
        f2=estado[3]
        if estado[3]>0:    
            f3=-g-(A/m)*rho*0.5*C_d*(estado[1]**2+estado[3]**2)
        else:
            f3=-g+(A/m)*rho*0.5*C_d*(estado[1]**2+estado[3]**2)
        return np.array([f0,f1,f2,f3]) 
#Ecuaion para el calculo del sistema inestable 
def EDOfi(estado,tiempo):
        f0=estado[1]
        f1=-(A/m)*rho*0.5*C_di*(estado[1]**2+estado[3]**2)
        f2=estado[3]
        if estado[3]>0:    
            f3=-g-(A/m)*rho*0.5*C_di*(estado[1]**2+estado[3]**2)
        else:
            f3=-g+(A/m)*rho*0.5*C_di*(estado[1]**2+estado[3]**2)
        return np.array([f0,f1,f2,f3])         

# Método de Euler para  resolver numéricamente la EDO 
def Euler(y,t,h,f): 
    y_s=y+h*f(y,t)
    y_c=y + h * (f(y,t)+ f(y_s,t+h))/2.0
    return y_c


# Ahora calculamos!
for j in range(N-1):
    y[j+1]=Euler(y[j],tiempo[j],h,EDO)
    yf[j+1]=Euler(yf[j],tiempo[j],h,EDOf)
    yfi[j+1]=Euler(yfi[j],tiempo[j],h,EDOfi)
    


x_datos=[y[j,0] for j in range(N)]
vx_datos=[y[j,1] for j in range(N)]
y_datos=[y[j,2] for j in range(N)]
vy_datos=[y[j,3] for j in range(N)]


xf_datos=[yf[j,0] for j in range(N)]
vxf_datos=[yf[j,1] for j in range(N)]
yf_datos=[yf[j,2] for j in range(N)]
vyf_datos=[yf[j,3] for j in range(N)]

xfi_datos=[yfi[j,0] for j in range(N)]
vxfi_datos=[yfi[j,1] for j in range(N)]
yfi_datos=[yfi[j,2] for j in range(N)]
vyfi_datos=[yfi[j,3] for j in range(N)]

#_________________________________________________________________________________________
plt.plot(tiempo,y_datos,'orange', label="Sin friccion")
plt.plot(tiempo,yf_datos,'blue', label="Con friccion estable")
plt.plot(tiempo,yfi_datos,'yellow', label="Con friccion inestable")
plt.legend(["Sin friccion", "Con friccion estable", "Con friccion instable"], loc="upper left") 
plt.ylim(0,max(y_datos))
plt.xlabel('Tiempo[s]')
plt.ylabel('Posición[m]')
plt.show()

