"""4. Pedir al usuario un número entero y añadir todos los números
de la serie de fibonacci desde 0
hasta ese número (incluido) a una lista.
Mostrar dicha lista al acabar. Si el número introducido
es menor que 0, mostrar un mensaje de error."""

num = (int)(input("Introduce un número: "))
lista = [0,1]

if num < 0:
    print("Error")
else:
    for i in range(0,(num - 2)):
            lista.append(lista[-1] + lista[-2])

if num == 1:
    print(lista[0])
else:
    print(lista)