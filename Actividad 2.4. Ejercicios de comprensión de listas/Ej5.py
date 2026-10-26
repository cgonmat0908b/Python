"""5. Muestra la lista de los jugadores que saben hacer la filigrana "ruleta"."""
from listaJugadores import jugadores

ruleta = [j for j in jugadores for f in j["filigranas"] if f == "ruleta"]

print(ruleta)