def es_palindromo(texto : str) -> bool:
    cadenaVuelta = ""
    texto = texto.lower()
    texto = texto.replace(" ", "")

    for i in range(1,len(texto) + 1):
        cadenaVuelta += texto[len(texto) - i]

    return cadenaVuelta == texto


cadenaInversa = es_palindromo("Anita lava la tina")

print(cadenaInversa)