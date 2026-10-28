"""
6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
todas las series.
"""
from listaSeries import series

lista = ["La serie " + s["titulo"] + " tiene " + str(len(s["reseñas"])) + " reseñas" for s in series]

lista = [f"La serie {s['titulo']} tiene {len(s['reseñas'])} reseñas" for s in series]

print(lista)