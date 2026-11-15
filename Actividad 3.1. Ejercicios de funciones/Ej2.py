"""
2. Crea una función llamada convertirTemperatura que reciba un número con
decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
serán “C”, “K” y “F”, que representan unidades de temperatura (Celsius,
Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
resultado de convertir de la primera unidad que reciba la función a la
segunda. Por ejemplo, convertirTemperatura(10,”F”,”C”) devolvería el
resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos
decimales, redondeando al valor más cercano.
"""

# is_digit(string) recibe un string y comprueba si es un ENTERO
#subString en Python ejemplos cadena1 = "Hola paquito" => cadena2 = cadena1[0:2] cadena2 "Hol" cadena1[:5] => de 0 a 5 cadena1[5:] desde el 5 hasta el último 
# round(a,b) a = numero a redondear, b = numero de  decimales
# floor() redondea hacia abajo, ceil() redondea hacia arriba


def convertirTemperatura(tempEntrada, unidadEntrada, unidadConvertir):
    unidadesValidas = ["C","K","F"]
    tempFinal = 0

    if unidadEntrada in unidadesValidas and unidadConvertir in unidadesValidas and unidadEntrada != unidadConvertir:
        if unidadEntrada == "K":
            tempCelsius = tempEntrada - 273.15
        elif unidadEntrada == "F":
            tempCelsius = (tempEntrada - 32) / 1.8
        else:
            tempCelsius = tempEntrada

        if unidadConvertir == "C":
            tempFinal = round(tempCelsius , 2)
        elif unidadConvertir == "K":
            tempFinal = round(tempCelsius + 273.15 , 2)
        else:
            tempFinal = round((tempCelsius * 1.8) + 3 , 2)
    else:
        return "Algún valor es invalido"

    return f"{tempFinal:.2f}"

print(convertirTemperatura(0.0,"C","K"))