# Crear un programa que lea la edad de un usuario y muestre
# cuántos años tendrá dentro de tantos años como indique.


print("Calculo de edad futura")


edad=int(input(print("Por favor diga su edad actual:")))
tiempo=int(input(print( "futuro a conocer:")))

edad_futura = edad + tiempo
print("La edad que tendrá en:", tiempo, "es:", edad_futura)