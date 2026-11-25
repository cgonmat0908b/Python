def convertir_acciones(compania, num_acciones, moneda):

    """Devuelve el valor de las acciones en la moneda elegida, con dos decimales."""

    # Valor de una acción de cada compañía, en euros

    valores = {"NVDA": 156.20, "SONY": 24.16, "BMW": 58.12}

    # Cuánto vale 1 euro en cada moneda de destino

    cambios = {"euro": 1.0, "dolar": 1.10, "libra": 0.83}

    # Normalizamos para no distinguir entre mayúsculas y minúsculas
    
    total_euros = valores[compania.upper()] * num_acciones

    return round(total_euros * cambios[moneda.lower()], 2)


def convertir_acciones(compania, num_acciones, moneda):
    # Pasamos los textos a un formato fijo para ignorar mayúsculas y minúsculas
    compania = compania.upper()
    moneda = moneda.lower()

    # Valor de una acción en euros
    if compania == "NVDA":
        valor = 156.20
    elif compania == "SONY":
        valor = 24.16
    elif compania == "BMW":
        valor = 58.12

    # Cuánto vale 1 euro en la moneda elegida
    if moneda == "euro":
        cambio = 1.0
    elif moneda == "dolar":
        cambio = 1.10
    elif moneda == "libra":
        cambio = 0.83

    return round(valor * num_acciones * cambio, 2)
