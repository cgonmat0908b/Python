# Recorrer un rango
for i in range (1,10,2):
    print(i)

# Recorrer lista de elementos
frutas = ["Melon", "Uva", "Sandia"]

for fruta in frutas:
    print(fruta)

# Recorrer diccionario
peliculas = (
    {"Titulo" : "Resident Evil", "nota" : 6},
    {"Titulo" : "Robocop" , "nota" : 8},
    {"Titulo" : "Terminator" , "nota" : 5},
    {"Titulo" : "Kárate a muerte en Torremolinos", "nota": 6}
)

for pelicula in peliculas:
    if pelicula["nota"] >= 7:
        print(pelicula["Titulo"])


# Recorrer string
texto = "Hola mundo"

for letra in texto:
    print(letra)

