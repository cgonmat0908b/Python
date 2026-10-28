"""
2. Muestra los títulos de las series que sean de Fantasía o Misterio.
"""
from listaSeries import series

lista = [s["titulo"] for s in series if "Fantasía" in s["generos"] or "Misterio" in s["generos"]]

print(lista)