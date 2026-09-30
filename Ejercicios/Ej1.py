nota = int(input("Introduce un número: "))

if nota <= 0 or nota > 10:
    print("Nota  invalida")
elif nota > 0 and nota < 5:
    print("Suspenso")
elif nota == 5:
    print("Aprobado")
elif nota == 6:
    print("Bien")
elif nota > 6 and nota < 9:
    print("Notable")
else:
    print("Sobresaliente")


match nota:
    case i if i < 0 or i > 10:
        print("Nota invalida")

    case 1 | 2 | 3 | 4:
        print("Supenso")

    case 5:
        print("Aprobado")

    case 6:
        print("Bien")

    case 7 | 8:
        print("Notable")

    case 9 | 10:
        print("Sobresaliente")