"""10. Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala."""
from listaJugadores import jugadores

listaFiligranas = [f for j in jugadores for f in j["filigranas"]]

print(listaFiligranas)


