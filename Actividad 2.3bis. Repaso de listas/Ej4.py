"""4. Muestra el título y la duración de todas las películas que sean de Fantasía y
Aventura al mismo tiempo. Hazlo con el formato del ejercicio 2."""

from listaPeliculas import peliculas

contadorGeneros = 0

for pelicula in peliculas:
    contadorGeneros = 0
    for genero in pelicula["generos"]:
        if genero == "Fantasía" or genero == "Aventura":
            contadorGeneros += 1
    if contadorGeneros == 2:
        print(pelicula["titulo"] , " " , pelicula["duracion"])