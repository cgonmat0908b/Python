"""1. Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
error. """

num = (int)(input("Introduce un número: "))
acum = 0

if num < 1:
    print("Error, número inferior a 1")
else:
    for i in range(num, 0, -1):
        acum += i

print(acum)