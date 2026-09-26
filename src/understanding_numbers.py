#Numero
#Enteros - Integers
"""
los numeros enteros los podemos sumar (+), 
restar(-), multiplicar(*) y dividir (/)
division entera //
potencias **n
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1 + number_2)

print("---------------------------------------------")

#potencias 
print(3**2) #3^2
print(3**3) #3^3
print(10**6) #10^6
print(10%2) # modulo (mod)


print("---------------------------------------------")
"numeros flotantes (reales)"
"""
son numeros con punto decimal 
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)
print(2/0.2)  


#imprimir la edad de alguien
age = 34 #variable del tipo int
#message= "charly tiene " + age + " años." "error cometido: usar strings con variable entero (int)"
message= "charly tiene " + str(age) + " años."
print(message)

print("---------------------------------------------")

"TYPE ERROR"
"""
TYPE ERROR: python no puede reconocer el tipo 
de informacion que se esta utilzando
"""
message_f = f"charly tiene {age} años."
print(message_f)

#metodo type
print(type(age), type("hola"), type(0.54), type(True))