# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 00:14:09 2021

@author: Daniela Osorio
"""

# Programa que le N numeros enteros y calcula la media y se cancelara cuando este sea negativo
# El nuemro iniciara en cero 
num=0
suma=0
media=0
canEle=0

num =  int(input("nuemro :"))# Lector del primer numero
while (num>0): # Inicio del ciclo 
    suma = suma  + num
    num = int(input("nuemro :"))# Resto de elementos 
    canEle = canEle+1
    
# Termina el ciclo
if canEle != 0:
    media = suma/canEle # Calcula la media
    print("la media es :", media ) 
    
else:
    print("no hay numeros para calcular ")
    