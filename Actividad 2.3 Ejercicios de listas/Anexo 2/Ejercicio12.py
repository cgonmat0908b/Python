"""12. Elimina todos los personajes cuya raza sea demonio."""

from listaFrieren import personajes_frieren

for personaje in personajes_frieren[:]:
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)

print(personajes_frieren)