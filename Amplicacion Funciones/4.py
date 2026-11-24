def es_vocal(letra : str) -> bool:
    letras = "aáeéiíoóuú"
    return letra.lower() in letras

def contar_vocales(palabra : str) -> int:
    numVocales = 0
    for letra in palabra:
        if es_vocal(letra):
            numVocales += 1
    return numVocales

print(contar_vocales("pAlAbrÁ"))