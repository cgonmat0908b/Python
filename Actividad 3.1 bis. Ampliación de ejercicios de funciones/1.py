"""

    1. Vamos a crear una función llamada aplicar_funcion que nos permita
    ejecutar el cálculo de varios algoritmos matemáticos.

    Crea primero una función sumatorio que reciba un número positivo (o cero) y
    devuelva el resultado de sumar todos los números desde el 0 hasta dicho
    número.

    Crea luego una función factorial que reciba un número igual o mayor a 1 y
    devuelva el resultado de multiplicar todos los números desde 1 hasta dicho
    número.

    Por último, crea la función aplicar_funcion, que reciba un valor numérico
    entero y un string. Si la cadena de texto introducida es “sumatorio”, ejecutará
    la función sumatorio con el valor pasado por parámetro, y si es “factorial”,
    ejecutará la función factorial. Así, si por ejemplo introducimos “3” y “factorial”,
    se devolverá el resultado “6”.

    Además, en caso de introducir un valor numérico no permitido, se mostrará
    un mensaje de error (por ejemplo, al introducir “-3” y “factorial”).

"""

def sumatorio(num):
    if num < 0:
        raise ValueError("Valor menor que 0")
    
    suma = 0

    for i in range(1,num + 1):
        suma += i
    return suma

def factorial(num):
    if num <= 0:
        raise ValueError("Número invalido, menor a 1")
    
    fact = 1

    for i in range(1,num + 1):
        fact *= i
    return fact

def aplicar_funcion(num,operacion):
    operacion = operacion.lower()

    if operacion not in ["sumatorio","factorial"]:
        raise ValueError("Operación no valida")

    if num < 1 and operacion == "factorial":
        raise ValueError("No se puede hacer el factorial de 0 o un número negativo.")

    resultado = 0

    if operacion == "factorial":
        resultado = factorial(num)
    elif operacion == "sumatorio":
        resultado = sumatorio(num)

    return resultado

print(aplicar_funcion(5,"sumatorio"))