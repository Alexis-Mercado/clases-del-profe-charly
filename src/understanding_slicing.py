print("\nuso del slicing".upper())
players = ["peter", "mercado", "aaron", "fatima", "renata"]
print("listas original: ", players)

#slicing
print(players[3:5]) #["fatima", "renata"]

"""
me permite trabajar con un grupo especifico de la lista:
al resultado se le conoce como un slice 
"""
#players = ["peter", "mercado", "aaron", "fatima", "renata"]
print("1:4", players [1:4] )
print(":3", players [:3] )
print("2:", players [2:] )
print("-3:", players [-3:] )
print("----------------------------casos especiales-------------------------------".upper())
print(players[1:10])
print(players[-10:10])
print(players[6:1])#no aparece nada
print(players[:0])#no aparece nada
print(players[0:1])

print("-----------------------loopin trhough a slice--------------------".upper())
students= ["peter", "mercado", "aaron", "fatima", "renata"]
for student in students[3:5]:
    print(f"el estudiane {student}, va apasar la materia.")
print(students)

#como copiar una lista
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food # manera erronea de copiar una lista

#tres maneras de copiar una lista 
#1 - utilizando slicing
my_friend_food_2 = my_food[:]
#2 - utilizando el metodo de las listas .copy()
my_friend_food_3 = my_food.copy()
#3 - utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)