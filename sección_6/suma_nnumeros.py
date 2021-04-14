
## programa que calcula la suma de los primeros n números naturales
def mostrar(x):
	i=0
	suma=x
	print("La suma de los 10 primeros Numeros Naturales")
	while i<x:
		i=i+1
		print(suma,"+",(x-i),"=",(suma+(x-i)))
		suma=suma+(x-i)
		
	return ()
numero=int(input("Ingrese los n primeros numeros a sumar:" ))
mostrar(numero)