print("-----------------------if statement-------------------------------")
#if statement
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars: 
    if car == "audi":
        print(car.upper())
    else:
        print(car)

print("-------------------el condicional verdadero--------------------")
#es el corazon del if

#para determinar igualdad ==
#condicional verdadero
truck = "ford"
print(truck == "ford") #true
print(truck == "Ford".lower())

#condicional falso
print("-------------------el condicional falso--------------------------")
print(truck=="cheyenne")


print("----------------el condicional para desigualdad-------------------")
print(truck!="tacoma") #true
print(truck!="ford") #false

print("-------------------comparaciones numéricas----------------------")
age = 34
print(age == 34) # true

print(age ==18) # false

print("-------------------comparaciones con if--------------------------")
answer = 17
if answer != 42:
    print("esa no es la respuesta correcta".title())

age = 19
#simbolo menor que
print(age < 21)#true
print(age <= 21) #true

#mayor que
print(age>21)
print(age>=21)
