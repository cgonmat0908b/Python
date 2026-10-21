from datos import personajes

def ejercicio1():
    personajes.append({
        "nombre": "Cell",
        "raza": "Androide Bio-Orgánico",
        "nivel_pelea": 10800,
        "tecnicas": ["Kamehameha", "Taiyoken", "Barrera de Energía"],
        "atributos": [{"fuerza": 88, "defensa": 92, "velocidad": 85}]
    })

def ejercicio2():
    mediaAtributos = 0
    for personaje in personajes:
        mediaAtributos = 0
        for atributo in personaje["atributos"]:
                for claveAtributo in atributo:  
                    mediaAtributos += atributo[claveAtributo]
        mediaAtributos /= len(atributo)
        if mediaAtributos > 80:
            print(personaje)

def ejercicio3():
    mediaVelocidad = 0
    contadorVelocidades = 0
    for personaje in personajes:
        for atributos in personaje["atributos"]:
            for clave in atributos:
                if clave == "velocidad":
                    mediaVelocidad += atributos[clave]
                    contadorVelocidades += 1
    mediaVelocidad /= contadorVelocidades

    for personaje in personajes:
        for atributos in personaje["atributos"]:
            for clave in atributos:
                if clave == "velocidad" and atributos[clave] > mediaVelocidad:
                    print(personaje)

def ejercicio4():
    for personaje in personajes:
        for tecnica in personaje["tecnicas"]:
            if tecnica == "Big Bang Attack":
                for atributos in personaje["atributos"]:
                    for clave in atributos:
                        if clave == "fuerza" and atributos[clave] <= 90:
                            atributos[clave] += 10
                        elif clave == "fuerza" and atributos[clave] > 90:
                            atributos[clave] = 100
        print(personaje["nombre"] , " " ,personaje["atributos"][0]["fuerza"])

def ejercicio5():
    fuerza_vegeta = 0

    for vegeta in personajes:
        if vegeta["nombre"] == "Vegeta":
            for atributo in vegeta["atributos"]:
                for clave in atributo:
                    if clave == "fuerza":
                        fuerza_vegeta = atributo[clave]

    for personaje in personajes:
        if personaje["nombre"] != "Vegeta":
            for atributo in personaje["atributos"]:
                for clave in atributo:
                    if clave == "defensa" and atributo[clave] < fuerza_vegeta:
                        print(personaje["nombre"], atributo[clave])

def ejercicio6():
    for personaje in personajes[:]:
        if personaje["raza"] == "Saiyajin":
            personajes.remove(personaje)

    print(personajes)
