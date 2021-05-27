# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:52:55 2021

@author: Daniela Osorio
"""

# Programa que calcula la nota de un estudinte 


# Entradas 
# Pedir el nombre del estudiante y sus 3 notas parciales 

canEst=int(input("Cantidad de estudiantes : "))
# Inicializar la variable que controla el ciclo
conRep=0
# Variable real para sumar las definitivas del grupo
sumaDefGru=0.0
# Variable para calcular la nota promedio del grupo
notProDefGru=0.0


while(conRep < canEst):
    # Intrucciones a repetir
    nomEst=input("Nombre Estudiante : " )
    notUnoEst=float(input("Parcial Uno: "))
    notDosEst=float(input("Parcial Dos: "))
    notTresEst=float(input("Prcial Tres: "))

    # Calculos 

    notDefEst = (notUnoEst+notDosEst+notTresEst)/3

    # Imprimir los resultados - Salida  
    print(f"1. la nota definitiva es : {notDefEst: .2f}")
    
    #Incrementar la variable que controla el ciclo
    conRep = conRep+1

#Calculo de suma definitiva
sumaDefGru = notDefEst+conRep
    
#Calcular el promedio del grupo
notProDefGru = sumaDefGru/canEst

#Imprimir la nota promedio del grupo
print(f"2. la nota promedio del grupo es : {notProDefGru: .2f}")

