radio = float(input("Ingrese el radio del círculo: "))
def areaperimetrocirculo(radio, pi=3.14): 
    area = pi * radio**2 
    perimetro = 2 * pi * radio
    return area, perimetro     
valor_area, valor_perimetro = areaperimetrocirculo(radio)
print("El área del círculo es: ", valor_area, "y su perímetro es", valor_perimetro)

areaperimetrocirculo(radio, pi=3.14)
