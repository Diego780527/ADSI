 
def factorial(x,n):
	if(n>0):
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x
 
numero = int(input("ingrese el numero a calcular: "))
calculo=factorial(1,numero)
print ("El factorial de %s es %s" % (numero,calculo))