"""
3. Cree un programa que reciba dos números y muestre el mayor. 
En caso de que los números sean iguales también se debe mostrar al usuario. 
Use funciones. Haga pruebas de escritorio.
"""
numero1 = int(input("Ingrese primer número: "))
numero2= int(input("Ingrese segundo número: "))
def mayordedosnumeros(numero1,numero2): #PARÁMETROS
    if numero1 > numero2:
        print("El mayor es el primer número" ,numero1)
    elif numero1 < numero2:
        print("El mayor es el segundo número" ,numero2)
    else:
        print("El primer número:", numero1,  "y el segundo número:" , numero2, "son iguales" )   

mayordedosnumeros(numero1,numero2)   #ARGUMENTOS 
