"""7. Crea una copia de la lista llamada peliculas_infantiles e incluye en ella todas las
películas que tengan el género Infantil."""

from listaPeliculas import peliculas

peliculas_infantiles = []

for pelicula in peliculas:
    for genero in pelicula["generos"]:
        if genero == "Infantil":
            peliculas_infantiles.append(pelicula)

print(peliculas_infantiles)
        