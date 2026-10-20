"""14. A todos los personajes que pertenezcan a la Asociación Continental de Magia,
quítales esa afiliación."""

from listaFrieren import personajes_frieren

for personaje in personajes_frieren:
    for afiliado in personaje["afiliacion"][:]:
        if afiliado == "Asociación Continental de Magia":
            personaje["afiliacion"].remove(afiliado)

print(personajes_frieren)