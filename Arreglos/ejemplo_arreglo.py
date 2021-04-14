# for aplicado a un arreglo
#imprimir el listado de nombres que tiene almacenados

# Sin Arreglo
# Aca tenemos colecciones de datos
nombre1 ="María"
nombre2 ="Pedro"
nombre3 = "Raul"
nombre4 = "Luisa"
print(nombre1, nombre2, nombre3, nombre4)

#Con arreglos
arreglo_nombres = ["María, Pedro, Raul, Luisa"]
for nombre in arreglo_nombres:
    print("Nombres:", nombres)

#iteracion con range, usando len
#nos permite trabajar con el indice
#aca el rango del indice del arreglo que va a recorer

for i in range(0, 4):
    print("elemento:", arreglo_nombres)
