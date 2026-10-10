"""
TUPLAS
las tuplas son listas que no cambian de tamaño.
las tuplas son listas inmutables 

se utilizan los paraentesis () para definir una tupla

EJEMPLO:
    si tenemos un rectangulo (largo, ancho) que siempre va a tener cierto 
    tamaño, podemos asegurar que sus dimensiones no van a cambiar si colocamos 
    sus valores en una tupla
"""
dimensions = (200,50)#200 largo, 50 ancho
print("tupla original:", dimensions)

#vamos a imprimir elementos de una tupla
#se realiza de la misma forma que con una lista
print (dimensions[0])
print (dimensions[1])
print (dir(dimensions))
print("------------------------------lista---------------------------------------".upper())
#lisa 
dimensions_2 = [200,50]
print("metodos de las listas", dir (dimensions_2))

print("---------------------modificar una lista----------------------".upper())
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury"
names[1] = "mercury"
names[2] = "mercury"
print(names)

#dimension[0] = 500  error

print("------------------------------looping lista--------------------------------".upper())
#looping throgh a tuple
for dimension in dimensions:
    print(dimension)

"""
no podemos modificar una tupla,
los que si podemos hacer es cambiar 
la asignacion de una variable que 
almacena un tupla.
"""

dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)

print("-----------------------tipos de datos booleanos-----------------------".upper())
#tipos de datos booleanos
answer = True
print(answer)