num = (int)(input("Introduce un número: "))
contadorDivisibles = 0

for i in range(num, 0, -1):
    if(num % i == 0 ):
        contadorDivisibles += 1

if(contadorDivisibles > 2):
    print("No es un número primo")
else:
    print("Número primo")