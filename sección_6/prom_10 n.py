 
## programa que calcule el promedio de 10 números. 

def promedio(dato):
	prom=suma/10
	return (print("el promedio es de:",prom))

i=0
suma=0
while i < 10:
	dato =int(input("ingrese numero:" ))
	suma=suma+dato
	#print (suma)
	i=i+1
promedio(suma)
