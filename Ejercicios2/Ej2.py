"""2. Pedir al usuario un número entero y calcular el factorial
desde 1 hasta dicho número (incluido).
Si el número introducido es menor que 1, mostrar un mensaje de error."""

num = (int)(input("Introduce un número: "))
acum = num

if num < 1:
    print("Error, número inferior a 1")
else:
    for i in range(1, num):
        acum *= i

print(acum)