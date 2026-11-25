def convertir_acciones(compania : str, numAcciones : int, cambio : str) -> float:

    companiasPosibles = [
        "NVDA","SONY","BMW"
    ]

    monedas = [
        "euro", "dolar", "libra"
    ]
    
    compania = compania.upper()
    cambio = cambio.lower()

    valorAcciones = 0

    if compania == companiasPosibles[0]:
        valorAcciones = numAcciones * 156.2
    elif compania == companiasPosibles[1]:
        valorAcciones = numAcciones * 24.16
    elif compania == companiasPosibles[2]:
        valorAcciones = numAcciones * 58.12

    if cambio == monedas[1]:
        valorAcciones *= 1.1
    elif cambio == monedas[2]:
        valorAcciones *= 0.83
    elif cambio == monedas[0]:
        valorAcciones = valorAcciones

    return round(valorAcciones,2)