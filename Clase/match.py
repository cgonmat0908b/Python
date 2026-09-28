dia = input("Introduce un día: ")

match dia:
    case "lunes" | "miercoles":
        print("Hay clase")
    case "martes" | "jueves" | "viernes":
        print("No hay clases")
    case _:
        print("Error")

numero = int(input("Introduce un número: "))

# Match con comparaciones booleanas
match numero:
    case i if i < 0:
        print("Negativo")
    case i if i > 0:
        print("Positivo")
    case _:
        print("Cero")