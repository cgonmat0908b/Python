"""9. Muestra el nombre y la raza de todos los personajes que sean magos de primera
clase."""

from listaFrieren import personajes_frieren

for personajes in personajes_frieren:
    for afiliacion in personajes["afiliacion"]:
        if afiliacion == "Magos de Primera Clase":
            print(personajes)