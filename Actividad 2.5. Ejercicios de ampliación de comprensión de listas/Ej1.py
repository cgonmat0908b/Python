""" 
1. Muestra una lista con los títulos de las series que sean de Animación.
"""

from listaSeries import series

lista = [s["titulo"] for s in series if "Animación" in s["generos"]]
print(lista)