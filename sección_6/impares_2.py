 
##  programa que muestre los números impares entre 1 y n
def impar(x):
	i=0
	print("los numeros impares entes 1 y",x,"son:")
	while i<x:
		i=i+1
		print(i)
		i=i+1
	return ()

num=int(input("Ingrese el numero maximo "))
if num > 0:
	impar(num)
else:
	print ("ingrese un numero mayor que 0")