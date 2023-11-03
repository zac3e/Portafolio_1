#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:57:59 2023

@author: Diego Mendoza
"""

import numpy as np 
import matplotlib.pylab as plt
from matplotlib import cm
#Establecemos las constantes para el aluminio 
k=209.3
c_p=880
rho=2700
kappa=k/(rho*c_p)

L=1 #longitud total 
t_medicion=1500 #Tiempo de observacion 
n_x=30 #Numero de puntos de la coordenada x
n_t=900 #Numero de puntos de la coordenada y
 
delta_x= L/(n_x) #calculamos los pasos 
delta_t= t_medicion / (n_t)

#Creamos la matriz donde guardaremos nuestros valores de la temperatura
tempe=np.zeros((n_t+1,n_x+1))


#________________________________________________________________________________________________________________________________
#Establecemos las condiciones de frontera, que estan en primera y ultima columna de la matriz:
for i in range(n_t+1):
    tempe[i][0]=0
    tempe[i][n_x]=0
#Establecemos la Codicion inicial:
for i in range(1,n_x):
    tempe[0][i]=100
    
eta=(kappa * delta_t) / (delta_x)**2 #Calculasmos eta para poder ver si se cumple la condicion     
print(eta)    
for j in range(0,n_t): #Recorremos todas las filas 
    for i in range(1,n_x): #Por cada fila recorremos las columnas y asi poder recorrer toda la matriz 
        tempe[j+1][i]=tempe[j][i] + eta* (tempe[j][i+1] + tempe[j][i-1] - 2* tempe[j][i])
#_______________________________________________________________________________________________________________________
x = np.linspace(0, L, n_x+1)  #Usamos estos arrays para graficar 
y = np.linspace(0, t_medicion, n_t+1)
X,Y=plt.meshgrid(x,y) 
Z = tempe

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, rstride=1, cstride=1, alpha=0.8)
isotermas = [0,20, 50, 100] #Dejamos donde queremos las isotermas
contours = plt.contour(X, Y, Z, levels=isotermas, colors='black', linestyles='solid', linewidths=1)
cbar = fig.colorbar(surf, shrink=0.6, aspect=5) #Cremos una barra de colores
cbar.set_label('Temperatura')
ax.set_title("Superficie de temperatura (numerica)")
ax.set_xlabel('Posición [m]')
ax.set_ylabel('Tiempo [s]')
ax.set_zlabel('Temperatura [C]')
plt.show()







