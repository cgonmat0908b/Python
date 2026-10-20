"""3. A todas las películas que sean del género Drama, cámbiale la edad recomendada a
18."""

from listaPeliculas import peliculas

for pelicula in peliculas:
    for genero in pelicula:
        if genero == "Drama":
            pelicula["edad_recomendada"] = 18
            

print(peliculas)