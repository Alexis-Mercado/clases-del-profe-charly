"""
una lista comprehension combiena el for loop y la creacion 
de nueveos elementos en una sola linea y automaticamente agraga 
cada nuevo elemento a la lista, es decir, sin utilizar el metodo .append
"""
print("-------------elevacion al cuadrado--------------------")
squares=[value**2 for value in range(1,11)]
print(squares)

print("-------------elevacion al cuadrado--------------------")
names = ["renata", "balam", "sebas", "peter", "leo", "el chivo del avanico"]
names_upv = [name+ " @upv.edu.mx" for name in names]
print(names_upv)

print("-------------raiz cuadrada--------------------")
squares=[value//2 for value in range(1,11)]
print(squares)
