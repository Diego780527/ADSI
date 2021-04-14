# Cree un programa que lea dos números y muestre su producto,
# cociente, mdoulo su suma y su resta


print("Calculadora de enteros")

num1 = int(input("Digite el primer número:"))
num2 = int (input("Digite el segundo número:"))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
cociente = num1 // num2  # División normal
modulo = num1 % num2 # Division Residuo


print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado del producto es: ", producto)
print("El resultado del cociente es: ", cociente)
print("El resultado del modulo es: ", modulo)
