from datos import personajes

def ejercicio1():
    lista1 = [p["nombre"] for p in personajes if p["afiliacion"] == "Policía de Raccoon City" and p["vivo"] == True]
    print(lista1)

def ejercicio2():
    lista2 = [p["nombre"] for p in personajes if p["afiliacion"] == "Policía de Raccoon City" and "Pistola Samurai Edge" in p["armas"] and "Lanzagranadas" in p["armas"]]
    print(lista2)

def ejercicio3():
    lista3 = [(p["nombre"], p["afiliacion"]) for p in personajes if p["afiliacion"] != "Policía de Raccoon City"]
    print(lista3)

def ejercicio4():
    lista4 = [p["nombre"] + " (" + p["afiliacion"] + ")" for p in personajes if p["registro_misiones"]["misiones_completadas"] >= 20]
    print(lista4)

def ejercicio5():
    lista5 = [(p["nombre"], p["estatura_m"] * 100) for p in personajes if p["estatura_m"] > 1.70]
    print(lista5)

def ejercicio6():
    lista6 = [a for p in personajes for a in p["armas"]]
    print(lista6)

def ejercicio7():
    lista7 = [p["nombre"] for p in personajes if p["registro_misiones"]["zombies_solo"] + p["registro_misiones"]["zombies_equipo"] >= 100]
    print(lista7)

def ejercicio8():
    lista8 = [{"nombre" : p["nombre"], "zombies_totales" : p["registro_misiones"]["zombies_solo"] + p["registro_misiones"]["zombies_equipo"]} for p in personajes]
    print(lista8)

def ejercicio9():
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    print(media)

def ejercicio10():
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    lista10 = [(p["nombre"], p["estatura_m"]) for p in personajes if p["estatura_m"] > media]
    print(lista10)