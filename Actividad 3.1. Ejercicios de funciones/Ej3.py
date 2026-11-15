"""
3. Crea una función llamada calcularValorBruto, que reciba un número con
decimales (el precio de un producto) y una cadena de caracteres (que
representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
calcularValorBruto(10,”GENERAL”) devolvería el resultado de sumar a los
10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
hacia arriba.
"""

import math

# is_digit(string) recibe un string y comprueba si es un ENTERO
#subString en Python ejemplos cadena1 = "Hola paquito" => cadena2 = cadena1[0:2] cadena2 "Hol" cadena1[:5] => de 0 a 5 cadena1[5:] desde el 5 hasta el último 
# round(a,b) a = numero a redondear, b = numero de  decimales
# floor() redondea hacia abajo, ceil() redondea hacia arriba

def calcularValorBruto(precioProducto, tipoIVA):
    TIPOS_POSIBLES = ["GENERAL","REDUCIDO","SUPERREDUCIDO"]
    precioFinal = 0
    
    if tipoIVA in TIPOS_POSIBLES:
        if tipoIVA == TIPOS_POSIBLES[0]:
            precioFinal = precioProducto * 1.21
        elif tipoIVA == TIPOS_POSIBLES[1]:
            precioFinal = precioProducto * 1.1
        else:
            precioFinal = precioProducto * 1.04
        precioFinal = math.ceil(precioFinal * 100) / 100
    else:
        return "Algun valor es invalido."

    return f"{precioFinal:.2f}"

print(calcularValorBruto(1,"GENERAL"))