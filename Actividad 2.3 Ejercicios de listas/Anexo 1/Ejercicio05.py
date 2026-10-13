"""5. Muestra los pokémons que tengan un tipo que acabe en “a”."""

from listaPokemons import pokemons

for pokemon in pokemons:
    for tipos in pokemon["tipos"]:
        if tipos[-1] == "a":
            print(pokemon , "\n")
            break