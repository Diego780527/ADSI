## promedio de 3 notas de n estudiantes.
def promedio(estu,n1,n2,n3):
	prom=(n1+n2+n3)/3
	print("la nota promedio del estudiante",estu,"es:",prom)

estudiantes=int(input("Ingrese el numero de estudiantes: " ))+1
for i in range(1, estudiantes):
	nota1=int(input("Ingrese la Nota1 del estudiante:" ))
	nota2=int(input("Ingrese la Nota2 del estudiante:" ))
	nota3=int(input("Ingrese la Nota3 del estudiante:" ))
	promedio(i,nota1,nota2,nota3)