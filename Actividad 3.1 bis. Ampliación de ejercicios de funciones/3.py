"""

    3. Vamos a crear una función que permita convertir entre diferentes tipos de
    divisas.

    Crea una función llamada cambiar_divisa que reciba como parámetros una
    cantidad de dinero (que puede tener decimales), un string que represente la
    divisa en la que está, y otro string que represente la divisa en la que
    queramos convertir el dinero.
    
    La función devolverá el equivalente en la segunda divisa del dinero especificado
    en la primera divisa.

    Así, la función cambiar_divisa(10, “euro”, “dolar”) devolverá 10’90 dólares.

    Las divisas se escribirán sin tilde y será indiferente que estén en mayúsculas
    o minúsculas.

    La función permitirá cambiar entre euros, dólares y yenes, y devolverá el
    resultado con 3 decimales. A continuación tienes los tipos de cambio entre
    estas divisas:

"""

def cambiar_divisa(cantidadDinero : float, divisaActual : str, divisaCambio : str) -> float:
    
    """
        Función que dada una cantidad de dinero, la divisa en la que se encuentra y la divisa
        a cambiar, realiza el cambio de valor.

        Args:
            cantidadDinero (float): Cantidad de dinero del usuario
            divisaActual (str): Divisa actual del dinero del usuario
            divisaCambio (str): Divisa en la que se desea el dinero

        Returns:
            float: Devuelve la moneda cambiada a la divisa seleccionada
    """

    divisas = ["euro","dolar","yen"]
    
    if  divisaActual.lower() not in divisas or divisaCambio.lower() not in divisas:
        raise ValueError("Divisas invalidas")

    euros = 0

    if divisaActual == "dolar":
        euros = cantidadDinero * 0.92
    elif divisaActual == "yen":
        euros = cantidadDinero * 0.0061
    else:
        euros = cantidadDinero

    if divisaCambio == "dolar":
        euros *= 1.09
    elif divisaCambio == "yen":
        euros *= 163.38

    return round(euros,3)

print(cambiar_divisa(10,"dolar","yen"))