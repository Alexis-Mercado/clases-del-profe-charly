# ==============================================================================
# HEADER / PORTADA
# ==============================================================================
# Student Name: Alexis Javier Mercado Ramírez
# Student ID / Matrícula: 2630024
# Group: IM 1-1
# Course: Data Structures and Collections in Python
# File Name: 2630024_MercadoRamirezAlexisJavier.py
# ==============================================================================

# ==============================================================================
# EXECUTIVE SUMMARY
# ==============================================================================
"""
RESUMEN EJECUTIVO:
Una lista y una tupla son colecciones en Python que se diferencian principalmente 
en su mutabilidad y forma de almacenamiento. Una lista es una colección ordenada 
y mutable (permite modificar, agregar o eliminar elementos), mientras que una tupla 
es ordenada pero inmutable (sus datos no pueden cambiar tras crearse). Validar rangos, 
índices existentes y colecciones vacías es indispensable para prevenir errores de 
ejecución. Este documento cubre problemas prácticos que resuelven operaciones 
con listas y cálculo de distancias con tuplas en contextos prácticos.
"""

# ==============================================================================
# PRINCIPLES AND BEST PRACTICES
# ==============================================================================
"""
PRINCIPIOS Y BUENAS PRÁCTICAS:
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
- Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
- Mantener un control estricto sobre los índices válidos para evitar errores de tipo IndexError.
- Escribir código legible y mensajes claros para el usuario.
"""

# ==============================================================================
# PROBLEM 1: Shopping list basics (list operations)
# ==============================================================================
"""
Problem 1: Shopping list basics (list operations)
Descripción: Administra una lista de productos y cantidades. Permite agregar un nuevo 
producto, contar el total de elementos y verificar si existe un producto específico.

Entradas:
- initial_items_text (string; ej. "apple,banana,orange")
- new_item (string)
- search_item (string)

Salidas:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validaciones:
- initial_items_text no debe estar vacío tras el strip.
- new_item y search_item no deben estar vacíos.

Casos de prueba:
1) Normal: initial = "apple, banana", new = "milk", search = "apple" -> Lista: ['apple', 'banana', 'milk'], Total: 3, Encontrado: true
2) Borde: initial = "apple", new = "apple", search = "orange" -> Lista: ['apple', 'apple'], Total: 2, Encontrado: false
3) Error: initial = "   ", new = "milk", search = "apple" -> Error: invalid input
"""

print("\n\t7.1 Problem 1: Shopping list basics (list operations)")

initial_items_text = input("Enter initial items separated by commas: ")
new_item_input = input("Enter a new item to add: ")
search_item_input = input("Enter an item to search: ")

cleaned_initial = initial_items_text.strip()
cleaned_new = new_item_input.strip()
cleaned_search = search_item_input.strip()

if not cleaned_initial or not cleaned_new or not cleaned_search:
    print("Error: invalid input")
else:
    items_list = [item.strip() for item in cleaned_initial.split(",")]
    items_list.append(cleaned_new)
    len_list = len(items_list)
    is_in_list = cleaned_search in items_list
    
    print(f"Items list: {items_list}")
    print(f"Total items: {len_list}")
    print(f"Found item: {str(is_in_list).lower()}")


# ==============================================================================
# PROBLEM 2: Points and distances with tuples
# ==============================================================================
"""
Problem 2: Points and distances with tuples
Descripción: Utiliza tuplas para representar dos puntos 2D (x1, y1) y (x2, y2), 
calcula la distancia euclidiana y genera una tupla con el punto medio.

Entradas:
- x1, y1, x2, y2 (coordenadas float)

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validaciones:
- Verificar que las entradas se puedan convertir a float.

Casos de prueba:
1) Normal: x1=0.0, y1=0.0, x2=3.0, y2=4.0 -> Distancia: 5.0, Punto medio: (1.5, 2.0)
2) Borde: x1=1.0, y1=1.0, x2=1.0, y2=1.0 -> Distancia: 0.0, Punto medio: (1.0, 1.0)
3) Error: x1=abc, y1=0.0, x2=1.0, y2=1.0 -> Error: invalid input
"""

print("\n\t7.2 Problem 2: Points and distances with tuples")

x1_input = input("Enter x1: ")
y1_input = input("Enter y1: ")
x2_input = input("Enter x2: ")
y2_input = input("Enter y2: ")

try:
    x1 = float(x1_input)
    y1 = float(y1_input)
    x2 = float(x2_input)
    y2 = float(y2_input)
    
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: {midpoint}")

except ValueError:
    print("Error: invalid input")


# ==============================================================================
# CONCLUSIONS
# ==============================================================================
"""
CONCLUSIONES:
- Las listas son ideales cuando necesitamos colecciones mutables y flexibles para agregar, eliminar o modificar elementos secuencialmente.
- Las tuplas proporcionan seguridad e inmutabilidad para datos estructurados fijos como coordenadas o registros inalterables.
- La validación previa de entradas y rangos previene errores de ejecución y asegura un comportamiento robusto en los programas.
"""

# ==============================================================================
# REFERENCES
# ==============================================================================
"""
Referencias:
1) Python Software Foundation. Built-in Types: list, tuple. 
   https://docs.python.org/3/library/stdtypes.html
2) Matthes, E. (2019). Python Crash Course: A Hands-On, Project-Based Introduction to Programming. No Starch Press.
3) Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.
4) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.
5) Python Documentation. Data Structures — Python 3 Documentation. 
   https://docs.python.org/3/tutorial/datastructures.html
"""