"""8. Crea una lista de tuplas con el nombre del jugador y el texto "Goleador" si su atributo
de tiro es mayor o igual a 9, o "Asistente" en caso contrario. Muéstrala."""
from listaJugadores import jugadores

goleadorAsitente = [(j["nombre"] , " Goleador" if j["atributos"]["tiro"] >= 9 else j["nombre"] , " Asistente")  for j in jugadores]

print(goleadorAsitente)