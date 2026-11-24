def analizar_texto(texto : str):

    listaPalabras = texto.split()
    # La palabra más larga se inicializa a la primera
    masLarga = listaPalabras[0]
    numVeces = 0
    vecesPorPalabra = []

    # Recorre cada palabra
    for palabra in listaPalabras:
        # Si la palabra es mas larga que la mas larga se reasigna
        if len(palabra) > len(masLarga):
            masLarga = palabra
        # Recorremos de nuevo las palabras
        for comprobarPalabra in listaPalabras:
            # Si la palabra del primer bucle vuelve a salir se suma al contador
            if palabra.lower() == comprobarPalabra.lower():
                numVeces += 1
        # Al acabar el segundo bucle sabremos cuantas veces a salido la palabra
        vecesPorPalabra.append(numVeces)
        # Volvemos el contador a 0
        numVeces = 0

    numVeces = max(vecesPorPalabra)

    return len(listaPalabras), masLarga, numVeces

print(analizar_texto("Hola hola HOLA mundo"))
    