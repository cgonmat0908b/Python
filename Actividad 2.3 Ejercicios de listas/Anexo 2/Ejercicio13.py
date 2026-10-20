"""13. Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python”"""

from listaFrieren import personajes_frieren

for personaje in personajes_frieren:
    if personaje["raza"] == "Elfo":
        personaje["afiliacion"].append("Elfos Supervivientes del Examen de Python")

print(personajes_frieren)