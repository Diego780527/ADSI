
producto= input("Ingrese el producto a comprar:")
def impuesto(p):
    if p== "crema" or p == "vino":
        return print("El producto paga IVA")
    
    if p== "arroz" or p =="lenteja":
        return print(p+ "articulo no paga iva")

    return print("Producto no existente")
impuesto(producto)