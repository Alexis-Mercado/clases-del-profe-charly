# ==============================================================================
# Portada
# Nombre: [Alexis Javier Mercado Ramírez]
# Matrícula: [2630024]
# Grupo: [IM 1-1]
# ==============================================================================

# ==============================================================================
# Resumen ejecutivo
# ==============================================================================
# Un string en Python es una secuencia inmutable de caracteres utilizada para 
# representar texto, lo que significa que no puede ser modificado "in situ".
# Permite realizar operaciones básicas como concatenación, obtención de longitud,
# extracción de subcadenas (slicing), búsqueda de patrones y reemplazo de texto.
# Validar y normalizar el texto de entrada (correos, nombres, contraseñas) es 
# fundamental para garantizar la integridad, seguridad y consistencia de los datos.
# Este documento cubre la implementación de 6 problemas prácticos que integran
# el diseño de entradas, salidas, validaciones estrictas y el uso de métodos de 
# strings con sus respectivos casos de prueba.
# ==============================================================================

# ==============================================================================
# Principios y buenas prácticas
# ==============================================================================
# - Los strings son inmutables: cualquier cambio genera una nueva cadena.
# - Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
# - Evitar "números mágicos" en índices; documentar qué extrae cada slice.
# - Usar métodos de string en lugar de reescribir lógica básica.
# - Diseñar validaciones claras: primero que no esté vacío, luego el formato.
# - Escribir código legible: nombres de variables claros y mensajes de error entendibles.
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# Description: Takes a full name string, normalizes spaces and capitalization, 
# and returns the name in Title Case along with its generated initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name: <Name In Title Case>
# - Initials: <X.X.X.>
#
# Validations:
# - full_name must not be empty after strip().
# - Must contain at least two words.
# - Cannot be only spaces.
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> Formatted: "Juan Carlos Tovar", Initials: "J.C.T."
# 2) Border: "ana   maria" -> Formatted: "Ana Maria", Initials: "A.M."
# 3) Error: "   " -> Error: invalid input
# ------------------------------------------------------------------------------

print('\n\t7.1 Problem 1: Full name formatter (name + initials)')
full_name = input("esctibe tu nombre: ".title())
print("\nNombre Registrado:", full_name)

cleaned_names = full_name.strip()
if not cleaned_names:
    print("Error: invalid input")

divide_names = cleaned_names.split()
if len(divide_names) < 2:
    print("Error: invalid input")
    
else:
    #toma la primera letra de cada palabra
    formatted_name = " ".join([name.capitalize() for name in divide_names])

    initials = "".join([f"{name[0].upper()}." for name in divide_names])
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
  
# ------------------------------------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# Description: Validates if an email address has a correct basic structure 
# containing a single '@' and a dot in the domain part without spaces.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email: true/false
# - Domain: <domain_part> (if valid)
#
# Validations:
# - email_text not empty after strip().
# - Exactly one '@' symbol.
# - No whitespace allowed.
# - At least one dot after '@'.
#
# Test cases:
# 1) Normal: "test@example.com" -> Valid email: true, Domain: example.com
# 2) Border: "user@domain.co.uk" -> Valid email: true, Domain: domain.co.uk
# 3) Error: "invalid-email.com" -> Valid email: false
# ------------------------------------------------------------------------------

print('\n\t7.2 Problem 2: Simple email validator (structure + domain)')
email_text = input("Escribe tu correo electrónico: ")
cleaned_email = email_text.strip()

if not cleaned_email:
    print("Valid email: false")
elif " " in cleaned_email:
    print("Valid email: false")
elif cleaned_email.count("@") != 1:
    print("Valid email: false")
else:
    at_index = cleaned_email.find("@")
    domain = cleaned_email[at_index + 1:]
    
    if "." not in domain:
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {domain}")

# ------------------------------------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Determines whether a given phrase reads the same forwards and 
# backwards, ignoring spaces and letter casing.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - Is palindrome: true/false
# - Normalized string display
#
# Validations:
# - phrase not empty after strip().
# - Minimum length of 3 characters after cleaning.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> Is palindrome: true
# 2) Border: "A man a plan a canal Panama" -> Is palindrome: true
# 3) Error: "Hi" -> Error: invalid input (too short)
# ------------------------------------------------------------------------------

print("\n\t7.3 Problem 3: Palindrome checker (ignoring spaces and case)")
phrase = input("Escribe una frase: ")
cleaned_phrase = phrase.strip()

if not cleaned_phrase:
    print("Error: invalid input")
else:
    normalized_phrase = cleaned_phrase.lower().replace(" ", "")
    
    if len(normalized_phrase) < 3:
        print("Error: invalid input (too short)")
    else:
        reversed_phrase = normalized_phrase[::-1]
        
        if normalized_phrase == reversed_phrase:
            print("Is palindrome: true")
            print(f"Normalized: {normalized_phrase}")
        else:
            print("Is palindrome: false")
            print(f"Normalized: {normalized_phrase}")

# ------------------------------------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# Description: Analyzes a sentence to calculate word count, identify the first 
# and last words, and find the shortest and longest words.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - Word count, First word, Last word, Shortest word, Longest word
#
# Validations:
# - sentence not empty after strip().
# - Must contain at least one valid word after split().
#
# Test cases:
# 1) Normal: "Python programming is very fun" -> Count: 6, First: Python, Last: fun
# 2) Border: "Hello" -> Count: 1, First: Hello, Last: Hello, Shortest: Hello, Longest: Hello
# 3) Error: "   " -> Error: invalid input
# ------------------------------------------------------------------------------

print('\n\t7.4 Problem 4: Sentence word stats (lengths and first/last word)')
sentence = input("Escribe una oración: ")
cleaned_sentence = sentence.strip()

if not cleaned_sentence:
    print("Error: invalid input")
else:
    words = cleaned_sentence.split()
    
    if len(words) == 0:
        print("Error: invalid input")
    else:
        word_count = len(words)
        print(f"Word count: {word_count}")
        
        first_word = words[0]
        print(f"First word: {first_word}")
        
        last_word = words[-1]
        print(f"Last word: {last_word}")
        
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)
        
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

# ------------------------------------------------------------------------------
# Problem 5: Password strength classifier
# Description: Evaluates a password and classifies its strength as weak, medium, 
# or strong based on length and character variety (upper, lower, digit, symbol).
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength: <weak/medium/strong>
#
# Validations:
# - Password must not be empty.
#
# Test cases:
# 1) Normal: "Secret123!" -> Password strength: strong
# 2) Border: "password" -> Password strength: weak
# 3) Error: "" -> Error: invalid input (empty password)
# ------------------------------------------------------------------------------

print('\n\t7.5 Problem 5: Password strength classifier')
password_input = input("Escribe tu contraseña: ")
if not password_input:
    print("Error: invalid input (empty password)")
else:
    length = len(password_input)
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  
            has_symbol = True

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    
    elif length < 8 or (not has_upper and not has_lower):
        print("Password strength: weak")
        
    else:
        print("Password strength: medium")

# ------------------------------------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# Description: Formats a product name and price into a fixed-width single-line 
# label of exactly 30 characters by padding or truncating.
#
# Inputs:
# - product_name (string)
# - price_value (string/number)
#
# Outputs:
# - Label: <exactly 30 characters>
#
# Validations:
# - product_name not empty after strip().
# - price_value must convert to a positive number.
#
# Test cases:
# 1) Normal: "Laptop", "1200.50" -> Label formatted to 30 chars
# 2) Border: "A", "5" -> Label padded to 30 chars
# 3) Error: "Phone", "-10" -> Error: invalid input (price must be a positive number)
# ------------------------------------------------------------------------------

print('\n\t7.6 Problem 6: Product label formatter (fixed-width text)')
product_name = input("Escribe el nombre del producto: ")
price_value = input("Escribe el precio del producto: ")

cleaned_name = product_name.strip()

if not cleaned_name:
    print("Error: invalid input (empty product name)")
else:
    try:
        numeric_price = float(price_value)
        if numeric_price < 0:
            raise ValueError("El precio no puede ser negativo")
        
        formatted_price = f"{numeric_price:.2f}"
        
        base_label = f"Product: {cleaned_name} | Price: ${formatted_price}"
        
        if len(base_label) > 30:
            final_label = base_label[:30]
        else:
            final_label = base_label.ljust(30)
            
        print(f"Label: \"{final_label}\"")
        print(f"Exact length: {len(final_label)}")
        
    except ValueError:
        print("Error: invalid input (price must be a positive number)")

# ==============================================================================
# Conclusiones
# ==============================================================================
# El manejo adecuado de strings es esencial en la entrada y salida de datos para
# asegurar la correcta interacción con el usuario. El uso de métodos como lower(),
# strip(), split() y join() facilita la limpieza y transformación eficiente del texto.
# Normalizar los datos antes de compararlos previene errores lógicos por variaciones 
# de formato o espacios adicionales. Asimismo, un diseño riguroso de validaciones
# evita la inserción de datos basura o inesperados. Finalmente, comprender la 
# inmutabilidad de las cadenas y el uso correcto de los slices permite manipular 
# la información con mayor seguridad y control de memoria.
# ==============================================================================

# ==============================================================================
# Referencias
# ==============================================================================
# 1) Python documentation - Built-in Types: Text Sequence Type — str
# 2) Lutz, M. (2013). Learning Python. O'Reilly Media.
# 3) Python Software Foundation. (2026). Built-in Functions - min(), max(), len()
# 4) Sweigart, A. (2019). Automate the Boring Stuff with Practical Programming.
# 5) Good Practices for Input Validation and Data Sanitization in Python.
# ==============================================================================