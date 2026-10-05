#trabajando con listas
print("\n\tel dia de hoy voy a trabajar con listas")
magicians = ['harry', 'ron',"hermione", "snape", "voldemor"]
print(magicians)

print("imprimir a la mala")
print(magicians[0],magicians[1], magicians[2], magicians[3], magicians[4])
print("----------------------------------------------------------------------")
#ciclo for
print("imprimir con 'for'".upper())
for magician in magicians:
    print(magician.upper(), end = " ")
    print()
    #estructura for + aux(singular) + in + iter (liste)
#a esto se le conoce como looping
#for cat in cats
#for item in items
print("-------------------------------------------------------------------------")
#magicians = ['harry', 'ron',"hermione", "snape", "voldemor"]
#ahora un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"no puedo esperar a ver el siguiene hechizo, {magician.upper()}\n")
print("gracias a todos. fue un gran espectaculo")

print("-------------------------------------------------------------------------")
#identacion
"""
python utiliza la identacion para determinar cuando 
una linea de codigo anterior.

basicamente, se utilzan 4 espacios en blanco para 
obligarnos a escribir codigo ordenado y estructurado
"""
#no olvidemos identar
magicians = ["alice", "david", "caroline"]
for magician in magicians:
    print(magician) #error de identacion 

#Error de logica - logic Error - identationError
for magician in magicians:
    print(magician) 
    print(f"no puedo esperar a ver el siguiente truco, {magician}")

#identacion innecesaria (espacio innecesario)
message = "hello python world!"
print(message)

#no olvidar los dos puntos - syntax error
for magician in magicians:
    print(magician)