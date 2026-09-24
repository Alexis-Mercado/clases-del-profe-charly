#let's try to use variables
message = "this is my first program:), i am very happy"
another_massage = "really, so so so so happy"

print(message)
print(another_massage)

print(message, another_massage)
print(message, another_massage)

message = "hi boys y girls"
print(message)

# mi nombre es Alexis Javier 
"""
REGLAS GENERALES PARA NOMBRA VARIABLES EN PYTHON

LOS NOMBRES DE VARIABLES SOLO DEBEN NOMBRERSE CON :
-palabras en ingles 
-numeros, letras y guion bajo
-deben comenzar con una letra o guion bajo, pero no con numeros
-No utilizar espacios para separar palbras(utilizar_)
-no utilizar palabras reservadas pe python o el nombre del archivo con nombre de variables 
-los nombres deben ser cortos pero descriptivos
letras minusculas, por ahora!!

EJEMPLO:
    CORRECTO : message_1, _message_1
    INCORRECTO: 1message_1, message 1

    TRACEBACK: es un registro donde el interprete tuvo problemas al intentar ejecutar el codigo

    NAMEERROR:sucede cuando olvidamos establecer el valor de una variable antes de utilizar o 
    cometimos un error ortografico al ingresar el nombre de la variable(typo).

"""

message = "hola amigo python"
print(message)



#STRINGS
"""Un string es de manera sencilla una serie de caracteres.
en python todo lo que se encuentre entre comillas simples 
"o dentro de comillas dobles" "es considerado un sting" 
Ejemplo:
    'esto es un string'
    "esto tambien es un string"
    'le dije a un amigo, "python es mi lenguaje favorito"'
    "el lenguaje 'python' lleva el nombre por monty python, no por la serpiente"

Ejemplo incorrecto:
    (x)"charly'
    (x)' "
"""

name = "aleXis jaVier merCado ramIrez"
print(name)

print(name.title()) #manera temporal
print(name)
name = name.title() #cambio ya establecido
print(name)

#metodos
"""
es una accion que python puede realizaar sobre una variable.

el punto . despues de la variable seguido por el nombre del 
metodo en este caso title() dice que se debe ejecutar el metodo title 
de la variable name.

Todos los metodos van seguidos de parentesis, porque en ocacionaes 
necesitan informacion adicional para funcionar. En eta ocacion, el 
metodo .title no requiere informacion adicional para ejecutarse.

solo puede con variables tipo string

"""

#otros metodos
print("----------------------------------------------------------------")
print(name.upper()) #todo en mayusculas
print(name.lower()) #todo en minusculas
print("----------------------------------------------------------------")
#COMBINACION (CONCATENACION) DE STRINGS 
print("COMBINACION O CONCATENACION DE STRINGS") 
first_name = "alexis"
last_name = "javier"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())

print("hola", first_name + " " + last_name)
print("hola".upper(), first_name.title() + " " + last_name)

print("--------------------------------------------------------------")
print("white space".title())
#white space
"""
Whitespace se refiere a cualquier caracter que no se imprime, es decir, un
espacio ( ), tabuladores(\t) y finales de linea(\n)

se utilizan para organizar las salidas de texto
"""
print("python")
print("\tpython")
print("\t\tpython")
print("lenguajes:\npython\nc\nJavascript")

print("--------------------------------------------------------------")

#f-string
famous_person = "charlymercury"
message = '     {famous_person} una vez dijo: python is love'
print(message)
message = f'   {famous_person} una vez dijo: python is love'
print(message)