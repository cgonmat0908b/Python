"""11. Inserta al final de la lista un nuevo personaje que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables)."""

from listaFrieren import personajes_frieren

listaCopia = personajes_frieren.copy()

listaCopia.append(
    {
        "nombre": "Cristian",
        "raza": "Humano",
        "clase": "Mago",
        "edad": 22,
        "afiliacion": ["Estudiante"]
    },
)

print(listaCopia)