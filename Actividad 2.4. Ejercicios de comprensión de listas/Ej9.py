"""9. Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas
distintas."""
from listaJugadores import jugadores

filigranas = [j["nombre"] for j in jugadores if len(j["filigranas"]) > 2]

print(filigranas)