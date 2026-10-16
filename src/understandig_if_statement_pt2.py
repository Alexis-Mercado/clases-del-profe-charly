"""
realizar un progara ma que determine el costo de un boleto a 
partir de las siguientes condiciones

-costo para una persona menor o igual a 4 años: gratis
-mayor a 4 y menor a 18: 200
mayor a 18: 500
"""
age = input("\ningresa tu edad: ")
#print(age)
#print(type(age))
age = int(age)
#print(type(age))

if age <= 4:
    cost = 0

if age >= 4 and age <18:
    cost = 200

if age >= 18:
    cost = 500

print(f"el costo del boleto es: {cost}")

print("------------------problema en 1 bloque de if----------------")
#if-elif-else
if age <= 4:
    cost = 0

elif age > 4 and age < 18:
    cost = 200

elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost=0
#else:
#    cost=0

print("bloque if-elif-else")
print(f"el costo del boleto es: {cost}")

