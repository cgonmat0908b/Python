"""8. Muestra la edad media de los personajes humanos."""

from listaFrieren import personajes_frieren

edadMedia = 0
contadorHumanos = 0

for personajes in personajes_frieren:
    if personajes["raza"] == "Humano":
        edadMedia += personajes["edad"]
        contadorHumanos += 1

edadMedia /= contadorHumanos

print("Edad media de los humanos: " , edadMedia)
