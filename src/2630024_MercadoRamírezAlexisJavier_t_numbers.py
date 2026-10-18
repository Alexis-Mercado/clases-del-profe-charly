# ==============================================================================
#PORTADA
# ==============================================================================
# Student Name: Alexis Javier Mercado Ramírez
# Student ID / Matrícula: 2630024
# Group: IM 1-1
# Course: Basic Programming in Python
# File Name: 2630024_MercadoRamirezAlexisJavier.py
# ==============================================================================

# ==============================================================================
# EXECUTIVE SUMMARY
# ==============================================================================
"""
EXECUTIVE SUMMARY:
En Python, los tipos int y float se diferencian en que los primeros manejan 
cantidades enteras sin decimales, mientras que los segundos procesan números 
reales con precisión fraccionaria. Un booleano (True/False) representa un valor 
de veracidad que se obtiene comúnmente a partir de comparaciones relacionales 
o evaluaciones lógicas. La validación de rangos y la prevención de divisiones 
entre cero son fundamentales para garantizar la estabilidad y robustez del software. 
Este documento cubre seis problemas prácticos que involucran conversiones de 
temperatura, cálculos de nómina con horas extra, elegibilidad de descuentos, 
estadísticas numéricas de enteros, aprobación de préstamos e índices de masa corporal (BMI), 
implementando validaciones de entrada, casting de tipos y toma de decisiones lógicas.
"""

# ==============================================================================
# PRINCIPLES AND BEST PRACTICES
# ==============================================================================
"""
PRINCIPLES AND BEST PRACTICES:
- Usar tipos apropiados: int para contadores, float para cantidades con decimales.
- Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
- Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
- Usar nombres de variables descriptivos y mensajes claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos (qué significa true y qué significa false en cada contexto).
"""

# ==============================================================================
# PROBLEM 1: Temperature converter and range flag
# ==============================================================================
"""
Problem 1: Temperature converter and range flag
Description: Converts a temperature in Celsius (float) to Fahrenheit and Kelvin, 
evaluating if it represents a high temperature (>= 30.0 °C).

Inputs:
- temp_c (float; temperature in °C)

Outputs:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validations:
- Verify that temp_c can be converted to float.
- Prevent physical impossibilities in Kelvin (temp_k < 0.0).

Test cases:
1) Normal: temp_c = 32.5 -> Fahrenheit: 90.50, Kelvin: 305.65, High temperature: true
2) Border: temp_c = 30.0 -> Fahrenheit: 86.00, Kelvin: 303.15, High temperature: true
3) Error: temp_c = -300.0 -> Error: invalid input (temperature below absolute zero)
"""

print("\n\t7.1 Problem 1: Temperature converter and range flag")

temp_c_input = input("Escribe la temperatura en celsius: ")
cleaned_temp = temp_c_input.strip()

if not cleaned_temp:
    print("Error: invalid input")
else:
    temp_c = float(cleaned_temp)
    
    # Realizar conversiones
    temp_f = temp_c * 9 / 5 + 32
    print(f"Fahrenheit: {temp_f:.2f}")
    
    temp_k = temp_c + 273.15
    print(f"Kelvin: {temp_k:.2f}")
    
    if temp_k < 0.0:
        print("Error: invalid input (temperature below absolute zero)")
    else:
        is_high_temp = temp_c >= 30.0
        print(f"High temperature: {str(is_high_temp).lower()}")


# ==============================================================================
# PROBLEM 2: Work hours and overtime payment
# ==============================================================================
"""
Problem 2: Work hours and overtime payment
Description: Calculates weekly pay. Up to 40 hours are paid at normal rate, 
and hours above 40 are paid at 150%. Includes a boolean flag for overtime.

Inputs:
- hours_worked (float)
- hourly_rate (float)

Outputs:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validations:
- hours_worked >= 0
- hourly_rate > 0
- Show "Error: invalid input" if constraints fail.

Test cases:
1) Normal: hours = 45.0, rate = 20.0 -> Regular: 800.00, Overtime: 150.00, Total: 950.00, Has overtime: true
2) Border: hours = 40.0, rate = 15.0 -> Regular: 600.00, Overtime: 0.00, Total: 600.00, Has overtime: false
3) Error: hours = -2.0, rate = 10.0 -> Error: invalid input
"""

print("\n\t7.2 Problem 2: Work hours and overtime payment")

hours_worked = input("total de horas trabajadas en la semana: ".title())
hourly_rate = input("pago por hora: ".title())
cleaned_hours = hours_worked.strip()
cleaned_hourly = hourly_rate.strip()

if not cleaned_hours and not cleaned_hourly:
     print("Error: invalid input")

else:
    hourly_rate = float(cleaned_hourly)
    hours_worked = float(cleaned_hours)

    if hours_worked < 0 or hourly_rate <=0:
        print("Error: invalid input")

    else:
        regular_hour = min(hours_worked, 40)
        overtime_hours = max(0.0, hours_worked - 40)

        regular_pay = regular_hour * hourly_rate
        print(f"Regular pay: {regular_pay:.2f}")

        overtime_pay = overtime_hours * hourly_rate * 1.5
        print(f"Overtime pay: {overtime_pay:.2f}")
        
        total_pay = regular_pay + overtime_pay
        print(f"Total pay: {total_pay:.2f}")

        has_overtime = hours_worked > 40
        print(f"Has overtime: {str(has_overtime).lower()}")


# ==============================================================================
# PROBLEM 3: Discount eligibility with booleans
# ==============================================================================
"""
Problem 3: Discount eligibility with booleans
Description: Determines if a customer gets a 10% discount based on student status, 
senior status, or a purchase total >= 1000.0.

Inputs:
- purchase_total (float)
- is_student_text (string: "YES" or "NO")
- is_senior_text (string: "YES" or "NO")

Outputs:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validations:
- purchase_total >= 0.0
- Normalize text inputs and ensure they are "YES" or "NO".

Test cases:
1) Normal: purchase = 1200.0, student = "NO", senior = "NO" -> Eligible: true, Final: 1080.00
2) Border: purchase = 1000.0, student = "NO", senior = "NO" -> Eligible: true, Final: 900.00
3) Error: purchase = 500.0, student = "MAYBE", senior = "NO" -> Error: invalid input
"""

print("\n\t7.3 Problem 3: Discount eligibility with booleans")

purchase_input = input("Total de la compra: ")
is_student_text = input("¿Es estudiante? (YES/NO): ")
is_senior_text = input("¿Es adulto mayor? (YES/NO): ")

cleaned_purchase = purchase_input.strip()
cleaned_student = is_student_text.strip().upper()
cleaned_senior = is_senior_text.strip().upper()

if cleaned_student != "YES" and cleaned_student != "NO":
    print("Error: invalid input")
elif cleaned_senior != "YES" and cleaned_senior != "NO":
    print("Error: invalid input")
elif not cleaned_purchase:
    print("Error: invalid input")
else:
    purchase_total = float(cleaned_purchase)
    
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:
        is_student = (cleaned_student == "YES")
        is_senior = (cleaned_senior == "YES")
        
        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        
        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total
            
        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total:.2f}")


# ==============================================================================
# PROBLEM 4: Basic statistics of three integers
# ==============================================================================
"""
Problem 4: Basic statistics of three integers
Description: Reads three integers and calculates sum, average, max, min, 
and a boolean flag indicating if all numbers are even.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validations:
- Verify that inputs can be converted to int.

Test cases:
1) Normal: n1 = 2, n2 = 4, n3 = 6 -> Sum: 12, Average: 4.00, Max: 6, Min: 2, All even: true
2) Border: n1 = 1, n2 = 2, n3 = 3 -> Sum: 6, Average: 2.00, Max: 3, Min: 1, All even: false
3) Error: n1 = 2.5, n2 = 4, n3 = 6 -> Error: invalid input
"""

print("\n\t7.4 Problem 4: Basic statistics of three integers")

n1_input = input("Escribe el primer número entero: ")
n2_input = input("Escribe el segundo número entero: ")
n3_input = input("Escribe el tercer número entero: ")

cleaned_n1 = n1_input.strip()
cleaned_n2 = n2_input.strip()
cleaned_n3 = n3_input.strip()

if not cleaned_n1 or not cleaned_n2 or not cleaned_n3:
    print("Error: invalid input")
else:
    n1 = int(cleaned_n1)
    n2 = int(cleaned_n2)
    n3 = int(cleaned_n3)
    
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")


# ==============================================================================
# PROBLEM 5: Loan eligibility (income and debt ratio)
# ==============================================================================
"""
Problem 5: Loan eligibility (income and debt ratio)
Description: Determines loan eligibility based on monthly income, debt ratio, and credit score.

Inputs:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validations:
- monthly_income > 0.0 (prevents division by zero)
- monthly_debt >= 0.0
- credit_score >= 0

Test cases:
1) Normal: income = 9000.0, debt = 2000.0, score = 700 -> Ratio: 0.22, Eligible: true
2) Border: income = 8000.0, debt = 3200.0, score = 650 -> Ratio: 0.40, Eligible: true
3) Error: income = 0.0, debt = 500.0, score = 700 -> Error: invalid input
"""

print("\n\t7.5 Problem 5: Loan eligibility (income and debt ratio)")

income_input = input("Ingreso mensual: ")
debt_input = input("Deuda mensual: ")
score_input = input("Puntaje de crédito: ")

cleaned_income = income_input.strip()
cleaned_debt = debt_input.strip()
cleaned_score = score_input.strip()

if not cleaned_income or not cleaned_debt or not cleaned_score:
    print("Error: invalid input")
else:
    monthly_income = float(cleaned_income)
    monthly_debt = float(cleaned_debt)
    credit_score = int(cleaned_score)
    
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
        
        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")


# ==============================================================================
# PROBLEM 6: Body Mass Index (BMI) and category flag
# ==============================================================================
"""
Problem 6: Body Mass Index (BMI) and category flag
Description: Calculates Body Mass Index (BMI) and provides category boolean flags.

Inputs:
- weight_kg (float)
- height_m (float)

Outputs:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validations:
- weight_kg > 0.0
- height_m > 0.0

Test cases:
1) Normal: weight = 70.0, height = 1.75 -> BMI: 22.86, Underweight: false, Normal: true, Overweight: false
2) Border: weight = 53.29, height = 1.70 -> BMI: 18.44, Underweight: true, Normal: false, Overweight: false
3) Error: weight = 0.0, height = 1.70 -> Error: invalid input
"""

print("\n\t7.6 Problem 6: Body Mass Index (BMI) and category flag")

weight_input = input("Peso en kilogramos (kg): ")
height_input = input("Estatura en metros (m): ")

cleaned_weight = weight_input.strip()
cleaned_height = height_input.strip()

if not cleaned_weight or not cleaned_height:
    print("Error: invalid input")
else:
    weight_kg = float(cleaned_weight)
    height_m = float(cleaned_height)
    
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0
        
        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")


# ==============================================================================
# CONCLUSIONS
# ==============================================================================
"""
CONCLUSIONS:
- Cómo los enteros y flotantes se usan de forma conjunta para cálculos reales.
- Cómo las comparaciones generan booleanos y permiten tomar decisiones (if).
- Por qué es importante validar rangos y evitar divisiones entre cero.
- Qué aprendiste sobre el diseño de condiciones combinadas con and, or, not.
- Cómo estos patrones se repiten en problemas de nómina, descuentos, préstamos, etc.
"""

# ==============================================================================
# REFERENCES
# ==============================================================================
"""
References:
1) Python documentation – Built-in Types: Numeric Types — int, float, complex
2) Python documentation – Boolean type — bool
3) Tutoriales de Python sobre operadores aritméticos, relacionales y lógicos.
4) Libros o apuntes de algoritmos y programación básica.
5) Artículos o apuntes de clase sobre validación de datos numéricos.
"""