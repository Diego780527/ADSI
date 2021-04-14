lado = int(input("Ingrese el lado (arista) del cubo en cm: "))
def volumen(lado): 
    v = lado *lado*lado 
    return v     
vol_cubo = volumen(lado) 
print("El Volúmen de un cubo con un lado (arista) de", lado, "centímetros es: ", volumen, "centímetros cúbicos: ") 

volumen(lado)