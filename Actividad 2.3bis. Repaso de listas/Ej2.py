"""2. Muestra el título y la duración de las películas con más duración que la media. Hazlo
con el formato título duración (por ejemplo: El Señor de los Anillos: La
Comunidad del Anillo 178)."""

from listaPeliculas import peliculas

meadiaDuracion = 0

for pelicula in peliculas:
    meadiaDuracion += pelicula["duracion"]

meadiaDuracion /= len(peliculas)

for pelicula in peliculas:
    if pelicula["duracion"] > meadiaDuracion:
        print(pelicula["titulo"] , " " , pelicula["duracion"])