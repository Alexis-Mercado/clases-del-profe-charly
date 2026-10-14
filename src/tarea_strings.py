def format_full_name():
    # Entrada de prueba (puedes cambiarla para probar normal, borde o error)
    full_name = "  juan carlos tovar  "
    
    # 1. Validación: eliminar espacios extremos y verificar si está vacío
    cleaned_name = full_name.strip()
    if not cleaned_name:
        print("Error: invalid input")
        return

    # 2. Separar el texto en palabras usando los espacios
    words = cleaned_name.split()
    
    # Validación: debe contener al menos dos palabras (nombre y apellido)
    if len(words) < 2:
        print("Error: invalid input")
        return

    # 3. Formatear el nombre completo en Title Case
    formatted_name = " ".join([word.capitalize() for word in words])
    
    # 4. Extraer las iniciales de cada palabra en mayúscula
    initials = "".join([f"{word[0].upper()}." for word in words])

    # 5. Mostrar las salidas con el formato requerido
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")

# Ejecutar la función
format_full_name()