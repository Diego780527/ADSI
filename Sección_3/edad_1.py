"""1. Cree un programa que lea la edad de un usuario e imprima un mensaje
 que diga si el usuario es mayor de edad o no. 
Use funciones. Haga pruebas de escritorio."""

edad = int(input("Ingrese su edad: "))
def edadusuario(edad): #PARÁMETROS
   if edad >= 18:
        print("Usted es mayor de edad, tiene", edad, "años")
   else:
        print("Usted es menor su edad, tiene", edad, "años")

edadusuario(edad) #ARGUMENTOS
