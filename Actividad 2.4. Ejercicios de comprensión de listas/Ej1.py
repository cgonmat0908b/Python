"""1. Muestra una lista solo con los nombres de todos los futbolistas."""
from listaJugadores import jugadores

mostrarLista = [jugador["nombre"] for jugador in jugadores]

print(mostrarLista)