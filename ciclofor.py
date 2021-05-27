# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:21 2021

@author: Daniela Osorio
"""

# Programa que lee una tabla y la imprime desde 1 hasta el 20 y sumolos resultados 

# Declarar Variable 
tabla = 0
multiplicador =1
resultado = 0
sumaResultado = 0 
conRepCiclo = 1

# leer el nuemro de la tabla para la cual vamos a realizar las operaciones 
tabla = int(input(" Tabla :"))
#leer el multiplicador 
multiplicador = int(input("Multiplicador :"))

# Inicio del ciclo
for conRepCiclo in range(multiplicador):
    print("en que vuelta va juan diego :", conRepCiclo)
    resultado = tabla * conRepCiclo
    sumaResultado = sumaResultado + resultado
    print(tabla, " * ",conRepCiclo, "=" ,resultado)
    #Incremento la variable  que controla el ciclo 
    conRepCiclo = conRepCiclo + 1    
# Se imprime la suma por fuera del ciclo
print("la suma de los resultados es : ", sumaResultado)
