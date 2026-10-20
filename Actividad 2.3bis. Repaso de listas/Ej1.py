"""1. Añade una película a la lista (con todos los datos completos)."""

from listaPeliculas import peliculas

peliculas.append(
    {
        "titulo": "Vengadores",
        "duracion": 154,
        "año_estreno": 2010,
        "edad_recomendada": 13,
        "generos": ["Super Heroes", "Acción"]
    },
)

print(peliculas)