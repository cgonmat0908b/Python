"""6. Inserta al final de la lista un nuevo pokémon que tenga todos
los campos con algún valor con sentido (puedes inventártelos
, pero que sean razonables)."""

from listaPokemons import pokemons

listaPokemonsMod = pokemons.copy()

listaPokemonsMod = [
    
    {

        "nombre": "Garchomp",
        "generacion": 4,
        "categoria": "Tiburon",
        "tipos": ["Tierra", "Dragón"],
        "peso_kg": 95.0,
        "altura_m": 1.9

    }
]

print("Pokemon añadido: " , listaPokemonsMod[-1])