"""4. Muestra el nombre y los tipos de los pokémons que sean de tipo agua."""

from listaPokemons import pokemons

for pokemon in pokemons:
    for tipos in pokemon["tipos"]:
        if tipos == "Agua":
            print("Nombre: " , pokemon["nombre"] , ", tipos: " , pokemon["tipos"])