#Agregando elementos a una lista
motorcycles = ['honda', "honda", 'yamaha']
print(motorcycles)

#metodo append
motorcycles.append("kawasaki")
print(motorcycles)

"""
el metodo append ayuda a crear listas facilmente de 
manera dinamica
"""
motorcycles_2 = [] #lista vacia
print (motorcycles_2) 

motorcycle = "ducati"
motorcycles_2.append("honda")
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
motorcycles_2.append(motorcycle)
print(motorcycles_2)
print("----------------------------------------------------------------------------------------")

#metodo .insert
motorcycles_2.insert(3,"BAJAJ")
print(motorcycles_2)
print("--------------------------------------------------------------------------------------------")

#METODO POP()
"""
elimina el ultimo elemento de la lista ,
pero nos permite utilizar el elemento despues de eliminarlo
"""
print("\n\t Aprendi a usar el metodo pop")
motorcycles_3 = ['honda', "suzuki", 'yamaha', "mortalica", 'kawasaki']
deleted_motorcycle = motorcycles_3.pop()
print(motorcycles_3)
print(f"tu moto borrada es: {deleted_motorcycle}".upper())
motorcycles_3.pop(2)
print(motorcycles_3)
print("-------------------------------------------------------------------------------------------")

#metodo remove
print("\n\t Aprendi a usar el metodo remove")
motorcycles_4 = ['honda', "suzuki", 'yamaha', "mortalica", 'kawasaki', "bajaj"]
motorcycles_4.remove("suzuki")
print(motorcycles_4)
print('------------------------------------------------------------------')

#ordenar listas
cars = ["bmw", "audi","toyota"]

cars.sort()