""" 2. Muestra la lista de los jugadores que llevan el dorsal número 10. """
from listaJugadores import jugadores

dorsal10 = [print(jugador) for jugador in jugadores if jugador["dorsal"] == 10]