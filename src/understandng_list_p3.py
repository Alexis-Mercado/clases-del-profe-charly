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

print("-------------------------------------------------------------------------")
#magicians = ['harry', 'ron',"hermione", "snape", "voldemor"]
#ahora un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"no puedo esperar a ver el siguiene hechizo, {magician.upper()}\n")
print("gracias a todos. fue un gran espectaculo")