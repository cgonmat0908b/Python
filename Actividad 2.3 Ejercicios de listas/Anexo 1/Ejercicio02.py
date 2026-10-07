"""2. Muestra la media de altura de todos los pokémons."""

from listaPokemons import pokemons

alturaPoke = 0
contador = 0

for pokemon in pokemons:
    alturaPoke += pokemon["altura_m"]
    contador += 1

alturaPoke /= contador

print("Altura media: " , alturaPoke)