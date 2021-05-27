# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:50:40 2021

@author: Daniela Osorio
"""

# Entradas 
# Programa que lee una tabla y la imprime desde 1 hasta el 20 y sumolos resultados 

# Declarar Variable 
tabla = 0
multiplicador = 1
resultado = 0
sumaResultados = 0 
conRepCiclo = 1

# leer el nuemro de la tabla para la cual vamos a realizar las operaciones 
tabla = int(input(" Tabla :"))
#leer el multiplicador 
multiplicador = int(input("Multiplicador :"))

# Inicio del ciclo repetitivo  WHILE
while(conRepCiclo <= multiplicador):
    resultado = tabla * conRepCiclo
    sumaResultados = sumaResultados + resultado
    print(tabla, " * ",conRepCiclo, "=" ,resultado)
    #Incremento la variable  que controla el ciclo 
    conRepCiclo = conRepCiclo + 1    
print("la suma de los resultados es : ", sumaResultados)
    