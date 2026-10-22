from datos import personajes

def ejercicio1():
    personajes.append(
        {
            "nombre": "Jorge Sanchez",
            "raza": "Alienigena",
            "ocupacion": "Cazador de seres",
            "estilo_combate": ["Respiración de abducción", "Respiración del Sol"],
            "atributos": {"fuerza": 89, "defensa": 87, "velocidad":60},
        }
    )

def ejercicio2():
    for personaje in personajes:
        mediaAtributos = 0

        for atributo in personaje["atributos"]:
            mediaAtributos += personaje["atributos"][atributo]

        mediaAtributos /= len(personaje["atributos"])

        if mediaAtributos > 85:
            print(personaje)

def ejercicio3():
    mediaFuerza = 0
    for personaje in personajes:
        mediaFuerza += personaje["atributos"]["fuerza"]

    mediaFuerza /= len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["fuerza"] > mediaFuerza:
            print(personaje)

def ejercicio4():
    for personaje in personajes:
        for estilo in personaje["estilo_combate"]:
            if estilo == "Respiración del Agua":
                if personaje["atributos"]["defensa"] > 90:
                    personaje["atributos"]["defensa"] = 100
                else:
                    personaje["atributos"]["defensa"] += 10
        print(personaje["nombre"], " " , personaje["atributos"]["defensa"])

def ejercicio5():
    fuerzaZenitsu = 0
    for personaje in personajes:
        if personaje["nombre"] == "Zenitsu Agatsuma":
            fuerzaZenitsu = personaje["atributos"]["fuerza"]
            break

    for personaje in personajes:
        if personaje["nombre"] != "Zenitsu Agatsuma" and personaje["atributos"]["defensa"] < fuerzaZenitsu:
            print(personaje["nombre"], " " , personaje["atributos"]["fuerza"] , " " , personaje["atributos"]["defensa"])


def ejercicio6():
    for personaje in personajes[:]:
        if personaje["ocupacion"] == "Cazador de demonios":
            personajes.remove(personaje)
    print(personajes)
