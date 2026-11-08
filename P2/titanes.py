from datos import personajes

def ejercicio1():
    lista1 = [p["nombre"] for p in personajes if p["afiliacion"] == "Cuerpo de Exploración" and p["vivo"] == True]
    print(lista1)

def ejercicio2():
    lista2 = [p["nombre"] for p in personajes if p["afiliacion"] == "Cuerpo de Exploración" and "Supervivencia" in p["habilidades"] and "Sigilo" in p["habilidades"]]
    print(lista2)

def ejercicio3():
    lista3 = [(p["nombre"], p["afiliacion"]) for p in personajes if p["afiliacion"] != "Cuerpo de Exploración"]
    print(lista3)

def ejercicio4():
    lista4 = [p["nombre"] + " (" + p["afiliacion"] + ")" for p in personajes if p["registro_combate"]["misiones_completadas"] >= 20]
    print(lista4)

def ejercicio5():
    lista5 = [(p["nombre"], p["estatura_m"] * 100) for p in personajes if p["estatura_m"] > 1.70]
    print(lista5)

def ejercicio6():
    lista6 = [h for p in personajes for h in p["habilidades"]]
    print(lista6)

def ejercicio7():
    lista7 = [p["nombre"] for p in personajes if p["registro_combate"]["titanes_solo"] + p["registro_combate"]["titanes_equipo"] >= 5]
    print(lista7)

def ejercicio8():
    lista8 = [{"nombre" : p["nombre"], "titanes_totales" : p["registro_combate"]["titanes_solo"] + p["registro_combate"]["titanes_equipo"]} for p in personajes]
    print(lista8)

def ejercicio9():
    lista9 = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    print(lista9)

def ejercicio10():
    media = sum([p["estatura_m"] for p in personajes]) / len(personajes)
    lista10 = [(p["nombre"], p["estatura_m"]) for p in personajes if p["estatura_m"] > media]
    print(lista10)