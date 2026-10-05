"""5. Pedir al usuario un número y mostrar el triángulo de pascal
de ese número de filas.En caso de que el número 
sea inferior a 1, mostrar un mensaje de error."""

num = (int)(input("Introduce un número: "))

if num < 1:
    print("Error")
else:
    for i in range(0, num):
        for f in range(0,i):
            print()