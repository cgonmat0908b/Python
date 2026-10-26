"""3. Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona"."""
from listaJugadores import jugadores

barcelona = [j for j in jugadores if j["equipo"] == "FC Barcelona"]

print(barcelona)