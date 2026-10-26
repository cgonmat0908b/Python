""" 4. Muestra una lista con los nombres de los jugadores que tienen una puntuación de
pase igual o superior a 9 en sus atributos. """
from listaJugadores import jugadores

pase9 = [j for j in jugadores if j["atributos"]["pase"] >= 9]

print(pase9)