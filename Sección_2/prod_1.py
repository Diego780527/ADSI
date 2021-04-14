nombre_producto = str(input("Ingrese el nombre del producto: "))
precio_producto = int(input("Ingrese el precio del producto: "))
def producto(nombre_producto, precio_producto, DESCUENTO=0.10):
   precio_final_producto = precio_producto - precio_producto * 0.10 
return precio_final_producto 
valor_total_producto = producto(nombre_producto, precio_producto)
print("El precio final del producto con descuento del 10% es:", valor_total_producto, "pesos")

producto(nombre_producto, precio_producto, DESCUENTO=0.10)
