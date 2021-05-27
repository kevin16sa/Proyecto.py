# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:07:42 2021

@author: Daniela Osorio

Programa que lee el nombre y la nota de 3 materias (basic, fortan y pascal)
de N estudiantes.
condicion de salida nombre "***"
"""
# Area de declaracion de variable
var_e_nom="***"
var_e_bas=0.0
var_e_fort=0.0
var_e_pas=0.0
#Cantidad de estudiantes 
var_e_s_conEst=0
#media de notas
var_e_s_med=0.0

#Leer nombres estudiantes
var_e_nom=input("Digite nombre del estudiante :")


#Ciclo while
while(var_e_nom != "***"):
    var_e_bas= float(input("Definitiva Basic :"))
    var_e_fort= float(input("Definitiva Fortan :"))
    var_e_pas= float(input("Definitiva Pascal :"))
    
#Proceso que calcula la media del estudiante 
    var_e_s_med =(var_e_bas+var_e_fort+var_e_pas)/3
    print("la media :",var_e_s_med) 
    var_e_nom= input("Diite el nombre del estudiante ;")
    var_e_s_conEst = var_e_s_conEst+1
#Fin del ciclo
print("Total de estudiantes : ", var_e_s_conEst) 
print("Hallo :D")