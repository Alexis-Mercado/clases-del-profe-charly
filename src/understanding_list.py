"""
Las listas nos permten almacenar informacion en un
lugar la cantidad que se desee: ya sean pocos elementos 
o millones de elementos.

Una lista es una colección de items (elementos) que 
tienen un orden particular. se pueden crear listas que incluyan
strings, enteros, floats, podemos almacenar (los tipos de datos 
permitidos en Python) lo que queramos en una lista.

Son elementos mutables: puede modificar el tamaño ce la lista.

Se recomienda nombrar una variable del tipo lista en plural.

En Python, los corchetes [] indican una lista, sus elementos
se separan por comas.

Ejemplo:
"""

bicycles = ["trek", 'cannondale', "redline", 'specialized', "apache"]
print (bicycles[3])

#como podemo acceder a los elementos de una lista?
"""
Las listas son colecciones ordenadas. se puede acceder a un elemento de una 
lista diciendole a Python la posición o indice del elemento deseado.

para obtenner el valor deseado, se debe escribir el nombre de la lista,
seguido del indce del elemento entre corchetes.
"""
print (bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

#los indices comienzan en 0, no en 1
#bicycles = ["trek", 'cannondale', "redline", 'specialized', "apache"]
#ejemplo
print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])
print(bicycles[-2])

#Utilizando valores individuales de una lista 
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)

