"""3. Muestra el nombre y la altura de todos los pokémons
que midan menos que la media."""

from listaPokemons import pokemons

alturaPoke = 0
contador = 0

for pokemon in pokemons:
    alturaPoke += pokemon["altura_m"]
    contador += 1

alturaPoke /= contador

for pokemon in pokemons:
    if pokemon["altura_m"] < alturaPoke:
        print(pokemon["altura_m"] , " " , pokemon["nombre"])