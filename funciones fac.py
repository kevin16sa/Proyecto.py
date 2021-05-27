# Factura de ventas 

#Definicion de variables 
ve_nomArt=""
ve_canART=0
ve_valUniArt=0.0


cons_porIva=0.19

vps_netPag=0.0
vps_IvaPag=0.0
vps_totPag=0.0

#Entrada de datos 
ve_nomArt=input("nombre del artuculo:")
ve_canART=int(input("cantidad: "))
ve_valUniArt=int(input("volor: "))

#Procesos
vps_netPag= ve_canART*ve_valUniArt
vps_IvaPag= vps_netPag*cons_porIva
vps_totPag=vps_netPag+vps_IvaPag

# Salida 
print("Pagoneto:",vps_netPag)
print("valor iva:",vps_IvaPag)
print("total a pagar:",vps_totPag)