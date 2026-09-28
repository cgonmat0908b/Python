contador = 1

while contador <= 10:
    print(contador)
    contador += 1

    if contador == 5:
        print(contador)
        break

animales = ["Lince", "Gato", "Perro", "Gaviota"]

while animales:
    animal = animales.pop(0) #Guarda el primer valor y lo manda a la mierda de la lista
    print(animal)

