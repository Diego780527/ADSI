## programa que calcule la suma de los cuadrados de los números entre 1 y n

def cuad(dat):
	cuadrado=dat*dat
	#print(cuadrado)
	return (cuadrado)

i=0
suma=0
total=0
cant =int(input("numeros a sumar: " ))

while i<cant:
	dato =int(input("ingrese numero: " ))
	i=i+1
	t=cuad(dato)
	total=t+total
print ("la suma de los cuadrados es: ",total)