# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:28:52 2021

@author: Daniela Osorio
"""

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")