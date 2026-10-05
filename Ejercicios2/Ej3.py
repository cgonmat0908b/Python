"""3. Pedir al usuario dos números enteros (base y potencia)
Calcular el resultado de elevar la base al exponente.
Mostrar un error en caso de que la base sea menor que
1 o que la potencia sea menor que 0."""

base = (int)(input("Introduce un número: "))
potencia = (int)(input("Introduce otro número: "))
resultado = base

if base < 1 or potencia < 0:
    print("Error")
else:
    for i in range(1, potencia):
        resultado *= base

print(resultado)