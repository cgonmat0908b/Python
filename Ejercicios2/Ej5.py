"""5. Pedir al usuario un número y mostrar el triángulo de pascal
de ese número de filas.En caso de que el número 
sea inferior a 1, mostrar un mensaje de error."""

num = (int)(input("Introduce un número: "))

triangulo = []

# Construcción del triangulo
# Si el numero es menor a 1 error
if num < 1:
    print("Error")

else:
    #Creamos una fila vacia en cada iteración 
    for i in range(0, num):
        fila = []
        for f in range(0,i + 1):
            # Si f es la primera o última posición, añado a la primera o última un 1
            if f == 0 or f == i:
                fila.append(1)
            else:
                # Si no, añado a la posición actual el resultado de mirar en la anterior
                # fila, en la anterior posición de la actual y la sumo con la anterior fila,
                # la posición actual
                fila.append(triangulo[i - 1][f - 1] + triangulo[i - 1][f])
        # Tras completar la fila, lo añado al triangulo
        triangulo.append(fila)

# Variable para los espaciós para dar forma de piramide
numEspacios = num

for i in range(0, num):
    # Imprimo el número de espacios antes de que comience la fila
    print(" " * numEspacios, end="")
    for f in range(0, i + 1):
        # Imprimo la fila entera espaciada entre sí
        print(triangulo[i][f], end = " ")
    # Resto un espacio a la siguiente iteración para dar forma de piramide y añado un salto de linea
    numEspacios -= 1
    print()
        