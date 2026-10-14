"""7. Elimina todos los pokémons de tipo normal."""

from listaPokemons import pokemons

pokemonsCopia = pokemons.copy()

for pokemon in pokemonsCopia[:]: # pokemonsCopia[:] Los 2 puntos es una lista inmutable
    for tipos in pokemon["tipos"]:
        if tipos == "Normal":
            pokemonsCopia.remove(pokemon) 

print("Lista tras eliminación: " , pokemonsCopia)