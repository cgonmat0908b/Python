""" 6. Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9."""
from listaJugadores import jugadores

tiroRegate = [j for j in jugadores if j["atributos"]["tiro"] >= 8 and j["atributos"]["tiro"] >= 9]

print(tiroRegate)