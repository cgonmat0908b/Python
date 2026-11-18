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

def cambiar_divisa(cantidadDinero : float, divisaActual : str, divisaCambio : str):
    