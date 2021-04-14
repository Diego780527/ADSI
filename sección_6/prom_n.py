 
## programa que muestre el promedio de n números 

def promedio(dat,num):
	prom=suma/num
	return (print("el promedio es de:",prom))

i=0
suma=0
cant =int(input("ingrese numero de valores a promediar: " ))

while i<cant:
	dato =int(input("ingrese numero: " ))
	suma=suma+dato
	#print (suma)
	i=i+1
promedio(suma,cant)
