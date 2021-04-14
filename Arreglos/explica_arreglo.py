# Una lista es el conjunto ordenado de datos del mismo tipo (preferiblemente))
# Los elementos se encuentran ordenados por índice
# es una estructura de datos

#Sintaxis
# se crea el identificador, seguido del operador de
#asignacióm = , y entre corchetes
#separados por coma

numeros = [13, 14, 15, 200.5, -100]
#Arreglo lista vacía
Lista_vacia = []

#Lectura de elementos
# Ejemplo:
# se usa el identificador seguido de corchetes 
#que contiene el indice del elemento que se quiere
#leer

print"El elemento índice es: ", (numeros[3])

#Sobreescritura de elementos

print("----------------- Sobreescritura ---------")
# para asignar o sobreescribir elementos se usa el operador de asignacón =
# y le asignamos un nuevo valor
numeros[4] = 1000000
print("El indice modificado es:", nueneros[4])

print("------------------- borrado ------------------")

numeros.pop(4)
print("el elemento borrado es: ", numeros)

print("------------------- 2do borrado ------------------")


#se elimina el valor en punto medio de la lista
numeros.pop(1)
print("Elementos depués del segundo borrado es:", numeros)

print("------------------- Agregar elementos ------------------")

#para agregar elementos se usa el método append evaluado en el elemento que 
#queremos agregar

numeros.append(25)

# copia de arreglos
# debeemos usar el metodo copy

edades = [10, 15, 90, 20]
edades_copia = edades
print ("El contenido en copia de edades:"edades_copia)
edades.pop(2)
print ("El contenido modificado en copia de edades:"edades_copia)

print("****************** Copia independiente ***************")

edades_2 [100, 12, 19, 5]
copia_edades2 = edades_2.copy()

#operador len: sirve para longitudes de una cadena
# operador len aplicado a una cadena

cadena ="abczx"
print("Longitud de la cadena es:", len(cadena))

