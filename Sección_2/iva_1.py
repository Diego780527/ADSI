

def iva(a):
    impuesto = precio * 0,19
    total = precio + impuesto
    print("el artículo: ", articulo, "con un IVA de: ", impuesto", "Tiene como valor precio final:", total)

articulo=input("Digite el artículo: ")
precio=int(input("Digite el precio del articulo:"))

iva(precio)