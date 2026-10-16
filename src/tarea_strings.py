"""
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


print("\n\t7.4 Problem 4: Sentence word stats (lengths and first/last word)")
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


print("\n\t7.5 Problem 5: Password strength classifier")
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
"""

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