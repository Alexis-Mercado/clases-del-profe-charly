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
Una lista, una tupla y un diccionario son colecciones en Python que se diferencian 
principalmente en su mutabilidad y forma de almacenamiento. Una lista es una colección 
ordenada y mutable (permite modificar, agregar o eliminar elementos), mientras que 
una tupla es ordenada pero inmutable (sus datos no pueden cambiar tras crearse). 
Los diccionarios almacenan parejas de clave-valor para asociar identificadores únicos 
con información específica. Validar rangos, claves existentes y colecciones vacías 
es indispensable para prevenir errores de ejecución. Este documento cubre seis problemas 
prácticos que resuelven operaciones con listas, cálculo de distancias con tuplas, catálogos 
y calificaciones con diccionarios, conteo de frecuencias de palabras y un sistema CRUD 
de agenda de contactos.
"""

# ==============================================================================
# PRINCIPLES AND BEST PRACTICES
# ==============================================================================
"""
PRINCIPIOS Y BUENAS PRÁCTICAS:
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (por ejemplo, coordenadas, fechas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información por una clave (por ejemplo, por nombre, id, código).
- Evitar modificar una lista mientras la recorres con un for, a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios (por ejemplo, "name", "age", "price").
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
- "Lista de elementos:" <items_list>
- "Total de elementos:" <len_list>
- "Elemento encontrado:" true|false

Validaciones:
- initial_items_text no debe estar vacío tras el strip.
- new_item y search_item no deben estar vacíos.

Casos de prueba:
1) Normal: initial = "apple, banana", new = "milk", search = "apple" -> Lista: ['apple', 'banana', 'milk'], Total: 3, Encontrado: true
2) Borde: initial = "apple", new = "apple", search = "orange" -> Lista: ['apple', 'apple'], Total: 2, Encontrado: false
3) Error: initial = "   ", new = "milk", search = "apple" -> Error: entrada inválida
"""

print("\n\t7.1 Problema 1: Operaciones básicas con listas de compras")

initial_items_text = input("Ingresa los elementos iniciales separados por comas: ")
new_item_input = input("Ingresa un nuevo elemento para agregar: ")
search_item_input = input("Ingresa un elemento a buscar: ")

cleaned_initial = initial_items_text.strip()
cleaned_new = new_item_input.strip()
cleaned_search = search_item_input.strip()

if not cleaned_initial or not cleaned_new or not cleaned_search:
    print("Error: entrada inválida")
else:
    items_list = [item.strip() for item in cleaned_initial.split(",")]
    items_list.append(cleaned_new)
    len_list = len(items_list)
    is_in_list = cleaned_search in items_list
    
    print(f"Lista de elementos: {items_list}")
    print(f"Total de elementos: {len_list}")
    print(f"Elemento encontrado: {str(is_in_list).lower()}")


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
- "Punto A:" (x1, y1)
- "Punto B:" (x2, y2)
- "Distancia:" <distance>
- "Punto medio:" (mx, my)

Validaciones:
- Verificar que las entradas se puedan convertir a float.

Casos de prueba:
1) Normal: x1=0.0, y1=0.0, x2=3.0, y2=4.0 -> Distancia: 5.0, Punto medio: (1.5, 2.0)
2) Borde: x1=1.0, y1=1.0, x2=1.0, y2=1.0 -> Distancia: 0.0, Punto medio: (1.0, 1.0)
3) Error: x1=abc, y1=0.0, x2=1.0, y2=1.0 -> Error: entrada inválida
"""

print("\n\t7.2 Problema 2: Puntos y distancias con tuplas")

x1_input = input("Ingresa x1: ")
y1_input = input("Ingresa y1: ")
x2_input = input("Ingresa x2: ")
y2_input = input("Ingresa y2: ")

try:
    x1 = float(x1_input)
    y1 = float(y1_input)
    x2 = float(x2_input)
    y2 = float(y2_input)
    
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    
    print(f"Punto A: {point_a}")
    print(f"Punto B: {point_b}")
    print(f"Distancia: {distance:.2f}")
    print(f"Punto medio: {midpoint}")

except ValueError:
    print("Error: entrada inválida")


# ==============================================================================
# PROBLEM 3: Product catalog with dictionary
# ==============================================================================
"""
Problem 3: Product catalog with dictionary
Descripción: Administra un catálogo de productos mediante un diccionario donde las 
claves son nombres de productos y los valores son precios unitarios. Calcula el total.

Entradas:
- product_name (string)
- quantity (int)

Salidas:
- Si existe: "Precio unitario:", "Cantidad:", "Total:"
- Si no existe: "Error: producto no encontrado"

Validaciones:
- product_name no vacíos.
- quantity > 0.

Casos de prueba:
1) Normal: producto = "apple", cantidad = 3 -> Precio unitario: 10.0, Cantidad: 3, Total: 30.0
2) Borde: producto = "milk", cantidad = 1 -> Precio unitario: 25.5, Cantidad: 1, Total: 25.5
3) Error: producto = "laptop", cantidad = 2 -> Error: producto no encontrado
"""

print("\n\t7.3 Problema 3: Catálogo de productos con diccionario")

product_prices = {"apple": 10.0, "banana": 5.5, "milk": 25.5, "bread": 18.0}

product_input = input("Ingresa el nombre del producto: ")
quantity_input = input("Ingresa la cantidad: ")

cleaned_product = product_input.strip().lower()
cleaned_quantity = quantity_input.strip()

if not cleaned_product or not cleaned_quantity:
    print("Error: entrada inválida")
else:
    try:
        quantity = int(cleaned_quantity)
        
        if quantity <= 0:
            print("Error: entrada inválida")
        elif cleaned_product in product_prices:
            unit_price = product_prices[cleaned_product]
            total_price = unit_price * quantity
            
            print(f"Precio unitario: {unit_price}")
            print(f"Cantidad: {quantity}")
            print(f"Total: {total_price:.2f}")
        else:
            print("Error: producto no encontrado")
            
    except ValueError:
        print("Error: entrada inválida")


# ==============================================================================
# PROBLEM 4: Student grades with dict and list
# ==============================================================================
"""
Problem 4: Student grades with dict and list
Descripción: Administra un diccionario que vincula nombres de estudiantes con listas 
de calificaciones, calcula su promedio y verifica si aprobaron (promedio >= 70.0).

Entradas:
- student_name (string)

Salidas:
- Si existe: "Calificaciones:", "Promedio:", "Aprobado:"
- Si no existe: "Error: estudiante no encontrado"

Validaciones:
- student_name no vacío.
- Lista de calificaciones no vacía.

Casos de prueba:
1) Normal: estudiante = "Alice" -> Calificaciones: [90.0, 85.0], Promedio: 87.50, Aprobado: true
2) Borde: estudiante = "Bob" -> Calificaciones: [70.0, 70.0], Promedio: 70.00, Aprobado: true
3) Error: estudiante = "John" -> Error: estudiante no encontrado
"""

print("\n\t7.4 Problema 4: Calificaciones de estudiantes con diccionario y lista")

student_grades = {
    "alice": [90.0, 85.0],
    "bob": [70.0, 70.0],
    "charlie": [50.0, 60.0]
}

student_input = input("Ingresa el nombre del estudiante: ")
cleaned_student = student_input.strip().lower()

if not cleaned_student:
    print("Error: entrada inválida")
elif cleaned_student in student_grades:
    grades_list = student_grades[cleaned_student]
    
    if len(grades_list) == 0:
        print("Error: entrada inválida")
    else:
        average_val = sum(grades_list) / len(grades_list)
        is_passed = average_val >= 70.0
        
        print(f"Calificaciones: {grades_list}")
        print(f"Promedio: {average_val:.2f}")
        print(f"Aprobado: {str(is_passed).lower()}")
else:
    print("Error: estudiante no encontrado")


# ==============================================================================
# PROBLEM 5: Word frequency counter (list + dict)
# ==============================================================================
"""
Problem 5: Word frequency counter (list + dict)
Descripción: Cuenta la frecuencia de aparición de cada palabra en una oración 
usando una lista y un diccionario, y determina la palabra más frecuente.

Entradas:
- sentence (string)

Salidas:
- "Lista de palabras:" <words_list>
- "Frecuencias:" <freq_dict>
- "Palabra más común:" <word>

Validaciones:
- sentence no vacía tras el strip.

Casos de prueba:
1) Normal: oración = "apple banana apple" -> Lista: ['apple', 'banana', 'apple'], Frecuencias: {'apple': 2, 'banana': 1}, Más común: apple
2) Borde: oración = "python" -> Lista: ['python'], Frecuencias: {'python': 1}, Más común: python
3) Error: oración = "   " -> Error: entrada inválida
"""

print("\n\t7.5 Problema 5: Contador de frecuencias de palabras")

sentence_input = input("Ingresa una oración: ")
cleaned_sentence = sentence_input.strip()

if not cleaned_sentence:
    print("Error: entrada inválida")
else:
    words_list = cleaned_sentence.lower().split()
    
    if len(words_list) == 0:
        print("Error: entrada inválida")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
                
        max_freq = -1
        most_common = ""
        for word, freq in freq_dict.items():
            if freq > max_freq:
                max_freq = freq
                most_common = word
                
        print(f"Lista de palabras: {words_list}")
        print(f"Frecuencias: {freq_dict}")
        print(f"Palabra más común: {most_common}")


# ==============================================================================
# PROBLEM 6: Simple contact book (dictionary CRUD)
# ==============================================================================
"""
Problem 6: Simple contact book (dictionary CRUD)
Descripción: Implementa una pequeña agenda de contactos permitiendo operaciones 
de agregar (ADD), buscar (SEARCH) y eliminar (DELETE).

Entradas:
- action_text ("ADD", "SEARCH", o "DELETE")
- name (string)
- phone (string, solo para "ADD")

Salidas:
- "Contacto guardado:", "Teléfono:", "Contacto eliminado:", o "Error: contacto no encontrado"

Validaciones:
- action_text válido y normalizado en mayúsculas.
- name no vacío.

Casos de prueba:
1) Normal: acción = "ADD", nombre = "Alice", teléfono = "5551234" -> Contacto guardado: alice, 5551234
2) Borde: acción = "SEARCH", nombre = "Alice" -> Teléfono: 5551234
3) Error: acción = "DELETE", nombre = "Unknown" -> Error: contacto no encontrado
"""

print("\n\t7.6 Problema 6: Agenda de contactos básica (CRUD)")

contacts_dict = {"alice": "1234567890", "bob": "9876543210"}

action_input = input("Ingresa la acción (ADD, SEARCH, DELETE): ")
action_text = action_input.strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: entrada inválida")
else:
    name_input = input("Ingresa el nombre del contacto: ")
    cleaned_name = name_input.strip().lower()
    
    if not cleaned_name:
        print("Error: entrada inválida")
    else:
        if action_text == "ADD":
            phone_input = input("Ingresa el número de teléfono: ")
            cleaned_phone = phone_input.strip()
            if not cleaned_phone:
                print("Error: entrada inválida")
            else:
                contacts_dict[cleaned_name] = cleaned_phone
                print(f"Contacto guardado: {cleaned_name}, {cleaned_phone}")
                
        elif action_text == "SEARCH":
            if cleaned_name in contacts_dict:
                print(f"Teléfono: {contacts_dict[cleaned_name]}")
            else:
                print("Error: contacto no encontrado")
                
        elif action_text == "DELETE":
            if cleaned_name in contacts_dict:
                contacts_dict.pop(cleaned_name)
                print(f"Contacto eliminado: {cleaned_name}")
            else:
                print("Error: contacto no encontrado")


# ==============================================================================
# CONCLUSIONS
# ==============================================================================
"""
CONCLUSIONES:
- Las listas son ideales cuando necesitamos colecciones mutables y flexibles para agregar o eliminar elementos.
- Las tuplas proporcionan seguridad e inmutabilidad para datos estructurados fijos como coordenadas o fechas.
- Los diccionarios permiten búsquedas instantáneas y eficientes mediante claves únicas de tipo llave-valor.
- Combinar estructuras, como diccionarios que contienen listas, facilita la organización y análisis de datos complejos.
- La validación previa de entradas y claves evita errores de ejecución y asegura un comportamiento robusto.
"""

# ==============================================================================
# REFERENCES
# ==============================================================================
"""
Referencias:
1) Python Software Foundation. Built-in Types: list, tuple, dict. 
   https://docs.python.org/3/library/stdtypes.html
2) Matthes, E. (2019). Python Crash Course: A Hands-On, Project-Based Introduction to Programming. No Starch Press.
3) Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical Programming for Total Beginners. No Starch Press.
4) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming. O'Reilly Media.
5) Python Documentation. Data Structures — Python 3 Documentation. 
   https://docs.python.org/3/tutorial/datastructures.html
"""