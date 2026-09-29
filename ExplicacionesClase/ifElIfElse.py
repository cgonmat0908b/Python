numero = int(input("Introduce un número\n"))

if numero > 0:
    print("Positivo")

elif numero < 0:
    print("Negativo")

else:
    print("Es 0")


dia = input("Introduce un día: ")

if dia == "lunes" or dia == "miercoles":
    print("Hay clase")
elif dia == "martes" or dia == "jueves" or dia == "viernes":
    print("No hay clase")
else:
    print("Error")