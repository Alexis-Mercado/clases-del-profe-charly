#listas de numeros
"""
las listas pueden almacenar numeros. Python ofrece variaas 
herramientas
"""
#metodo build-in range
"""
el metodo range() nos ayuda a crear facilmente series de numeros
Ejemplo:
"""
for value in range(1,5):
    print(value)
print("--------------------------------------------------------------------------------")

first_ten_numbers = range(0,10)
#print (type(first_ten_numbers))
for value in first_ten_numbers:
    print(value)
print("--------------------------------------------------------------------------------")

#crear una lista de numeros utilizando range
numbers = list(range(0,10))
print(numbers)
print("--------------------------------------------------------------------------------")

#lista de numeros pares
even_numbers = list(range(1,11,2))
#¿que pasa con un paso negativo?
print(even_numbers)
print("--------------------------------------------------------------------------------")
print('ejercicio'.upper())
five = list(range(5,51,5))
print(five)

print('------------------------------lista 10 numero cuadraticos------------------------'.upper())
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)