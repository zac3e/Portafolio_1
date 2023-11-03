#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:15:17 2023

@author: Diego Mendoza 
"""
import numpy as np #importamos numpy 
from scipy.special import spherical_jn #de scipy.special importamos las esfericas de besse
#Formulas de bessel:
#a)

def bessel_up(x,l): #Definimos nuestra funcion up, la cual presenta cancelacion sustractiva
    j_minus1=np.sin(x) / x #Asigamos el valor de la primera funcion 
    j_l=(np.sin(x) / x**(2)) - (np.cos(x) / x) #Asigamos el valor de la segunda funcion
    j_0=np.sin(x) / x #hacemos lo mismo que las ultimas dos lineas de codigo, pero esto para agregar estos valores a la lista
    j_1=(np.sin(x) / x**(2)) - (np.cos(x) / x)
    lista1=[j_0,j_1] #Definimos nuestra lista con los dos valores iniciales, que ira creciendo de tamaño
    for i in range(2,l+1): #vamos iterando el for dependiendo de valor de nuestra l 
        j_lplus1= ((2*i-1)/(x)) * j_l - (1/x)* j_minus1 * x  #Aplicamos la formula de recursion 
        lista1.append(j_lplus1) #Agregamos a la lista los nuervos valores calculados 
        j_minus1=j_l #definimos los nuevo parametros que se van recorriendo cada vez que se calcula un nuevo valor
        j_l=j_lplus1
    return lista1 #Por ultimo regresa la lista con todos los valores


def bessel_down(x,l): #Definimos la funcion down
    j_plus1=spherical_jn(l+1,x) #Establecemos como valores iniciales unos muy muy buenos
    j_l=spherical_jn(l,x) # Con la intencion de poder ver el poder del algortimo 
    j_minus1=0 #Inicializamos nuestra variable en 0 
    lista2=[j_l] #cremoas ina lista con el valor de j_{l} en ella
    for i in range(l-1,-1,-1): #Recorremos al reves el for para que vaya de arriba hacia abajo
        j_minus1= ((2*i+3)/(x)) * j_l - j_plus1 #Aplicamos la formula de recurrencia down
        lista2.append(j_minus1) #vamos agregando los valores que se calculan a la lista
        j_plus1=j_l #Vamos recorriendo los valores para que se vayan calculando las funciones
        j_l=j_minus1
    lista2.reverse() #como toprtillas voltteamos los elementos de la lista para poder imprimirlos en el mismo orden que la primera 
    return lista2

def valores(x,l): #definimos la funcion valores
    a = bessel_down(x, l) #establecemos a como la lista de valores de bessel down
    b = bessel_up(x, l)#establecemos b como la lista de valores de bessel up
    print(f"{'j(x)_{i}':<10}{'bessel_down':<25}{'bessel_up':<25}") #imprimimos uan cabecera a la posterioires columnas 
    for i, (ele_a, ele_b) in enumerate(zip(a, b), 0): #se recorre con i en el indice dictado por enumarate y la dupa recorre en zip
        print(f'{i:<10}{ele_a:<25}{ele_b:<25}')# donde zip es la funcion que compacta nuestras listas para poder recorrelas facilmente

for i in [0.1, 1, 10]: #Vamos llamando a la funcion valores para distintos valores de x
    print(f'Para x={i} tenemos que:')
    valores(i,25)
#_______________________________________________________________________________________________________________________________________
#b)
def bessel_down1(x,l):  #definimos nuestra funcion de "buenos" valores
    j_plus1=4.816080989237051e-33 #estos valores fueron corregidos una y otra vez 
    j_l=4.267413534767007e-34
    j_plus1_i=j_plus1 #definimos esta variable para poder coorregir los valores de entrada mejor 
    j_l_i=j_l         #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    j_minus1=0 #inicializamos la variable en el valor 0 
    lista4=[j_l] #creamos una lista con el valor de j_{l}
    for i in range(l-1,-1,-1): #vamos recorriendo la lista de arriba hacia abajo 
        j_minus1= ((2*i+3)/(x)) * j_l - j_plus1 #Aplicamos la formula de recurrencia down
        lista4.append(j_minus1) #vamos agregando los valores
        j_plus1=j_l #vamos recoerrieno los valores para ir generando los nuevos
        j_l=j_minus1
        if i==0:
            j_0=j_minus1
    factor= spherical_jn(0, x) / j_0 #Calculamos el factor para poder corregir los valores de entrada
    j_plus1_i=j_plus1_i * factor        #corregimos los valores de entrada
    j_l_i=j_l_i * factor    
    lista4.reverse()     #volteamos como tortilla la lista
    return j_l_i, j_plus1_i, lista4 #por ultimo regresamos los valores corregido y los elemntos calculados en la lista
#c_______________________________________________________________________________________________________________

l=25 #Establecemos cuantos elementos vamos a calcular 
_,_,lista_dow=bessel_down1(1,l) #asignamos lista_dow a la lista que nos manda el metodo bueno
lista_up=bessel_up(1,l)         # ""       lista_up a la lista quenos da el metodo de besse_up 
lista_dow2=[abs(x) for x in lista_dow] #hacemos una nueva lista pero con los valores absoluto de los elementos
lista_up2=[abs(x) for x in lista_up] #hacemos una nueva lista pero con los valores absoluto de los elementos
inferior=[] #Cremos las nuevas listas para los calculos que se necesitan para el cociente
superior=[]
cociente=[]
for i in range(l+1): #calculamos la parte superoir del cociente y vamos agregando los valores en la lista superior
    superior.append(abs(lista_dow[i] - lista_up[i]))
for i in range(l+1): #calculamos la parte inferioir del cociente y vamos agregando los valores en la lista inferior
    inferior.append(lista_dow2[i] + lista_up2[i])

for i in range(l+1): #por ultimo calculas el cociente y lo vamos agregando a la lista de cociente
    cociente.append(superior[i]/inferior[i])
cociente    
print(f"{'l':<10}{'bessel_down':<25}{'bessel_up':<25}{'cociente':<25}") #mandamos a imprimir todo para que quede bonito en 3 columnas
for i, (a,b,c) in enumerate(zip(lista_dow, lista_up, cociente), 0):
    print(f"{i:<10}{a:<25}{b:<25}{c:<20}")












