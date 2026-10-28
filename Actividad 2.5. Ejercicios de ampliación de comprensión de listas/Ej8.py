"""
8. Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las
notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso
contrario.
"""
from listaSeries import series

lista = [(s["titulo"], "Obra maestra" if acum >= 9 else "Gran serie") for s in series acum /= contador acum = 0 contador = 0 for r in s["reseñas"]  acum += r["nota"] contador += 1]