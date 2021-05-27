
#Calcula el cuadrado de los primeros 100 numeros 

#Area de declaracion de de variable 
cuadradoNumero=0
acuamuladoSuma=0
num=1

#Entradas 
cantidadNumero=int(input("Cantidad de Numeros: "))
#Proceso 
#Entradas
for num in range(cantidadNumero+1):
    cuadradoNumero=num*num
    acuamuladoSuma=acuamuladoSuma+cuadradoNumero
    print("el cuadrado de ; ", num, "es: ",acuamuladoSuma)

#Fin del ciclo
print("la suma de los cuadrados es:" ,acuamuladoSuma) 
   

    

