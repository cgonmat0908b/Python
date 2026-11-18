"""

2. Dada la lista de animales dispuesta más abajo, crea una función
comprobar_estado, que reciba el nombre de una especie y devuelva los
siguientes valores después de comprobar en la lista animales el número de
ejemplares que tiene:

● Si el número de ejemplares es 0, “Extinto”
● Si el número de ejemplares es mayor que 0 y menor o igual que 500, “En
peligro crítico”
● Si el número de ejemplares es mayor a 500 y menor o igual a 2000, “En
peligro”
● Si el número de ejemplares es mayor a 2000, “Amenazado”
● Si la especie no está en la lista, se lanzará una excepción con raise.
Será indiferente si el nombre de la especie está en mayúsculas o minúsculas.

animales = [
["Lobo ibérico", "Mamífero", 2500],
["Lince ibérico", "Mamífero", 1668],
["Quebrantahuesos", "Ave", 2000],
["Oso pardo", "Mamífero", 500]
]

"""
animales = [
["Lobo ibérico", "Mamífero", 2500],
["Lince ibérico", "Mamífero", 1668],
["Quebrantahuesos", "Ave", 2000],
["Oso pardo", "Mamífero", 500]
]

def comprobar_estado(nomEspecie : str) -> str:

    encontrado = False

    for listaAnimales in animales:
        if nomEspecie == listaAnimales[0]:
            encontrado = True

    if encontrado == False:
        raise ValueError("Animal no encontrado en la lista")

    estado = ""

    for listaAnimales in animales:
        if listaAnimales[2] == 0:
            estado = "Extinto"
        elif listaAnimales[2] > 0 and listaAnimales[2] <= 500:
            estado = "peligro crítico"
        elif listaAnimales[2] > 500 and listaAnimales[2] <= 2000:
            estado = "En peligro"
        elif listaAnimales[2] > 2000:
            estado = "Amenazado"

    return estado

print(comprobar_estado("Oso pardo"))