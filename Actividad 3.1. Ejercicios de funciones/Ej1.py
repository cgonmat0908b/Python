"""
1. Crea una función llamada comprobarLetraDNI que reciba una cadena de
caracteres que representará al DNI de una persona y devuelva True si el DNI
es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros
seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
conocer si la letra es correcta puedes consultar la web del Ministerio del
Interior.
"""

# isdigit(string) recibe un string y comprueba si es un ENTERO
#subString en Python ejemplos cadena1 = "Hola paquito" => cadena2 = cadena1[0:2] cadena2 "Hol" cadena1[:5] => de 0 a 5 cadena1[5:] desde el 5 hasta el último 
# round(a,b) a = numero a redondear, b = numero de  decimales
# floor() redondea hacia abajo, ceil() redondea hacia arriba

def comprobarLetraDNI():   


    dni = input("Introduce un DNI:")
    correcto = False

    if len(dni) == 9:
        numeros = dni[0:8]
        letra = dni[8].upper()

        letrasDNI = [
            'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F',
            'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S',
            'Q', 'V', 'H', 'L', 'C', 'K', 'E'
        ]

        if numeros.isdigit() and letra in letrasDNI:
            numeros = int (numeros)
            if letra == letrasDNI[numeros % 23]:
                correcto = True


    return correcto

dniCorrecto = comprobarLetraDNI()

if dniCorrecto:
    print("Dni valido")
else:
    print("Dni invalido")