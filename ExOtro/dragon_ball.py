from datos import personajes

def ejercicio1():
    personajes.append({
        "nombre": "Cell",
        "raza": "Androide Bio-Orgánico",
        "nivel_pelea": 10800,
        "tecnicas": ["Kamehameha", "Taiyoken", "Barrera de Energía"],
        "atributos": {"fuerza": 88, "defensa": 92, "velocidad": 85}
    })


def ejercicio2():
    for personaje in personajes:
        mediaAtributos = 0

        for atributo in personaje["atributos"]:
            mediaAtributos += personaje["atributos"][atributo]

        mediaAtributos /= len(personaje["atributos"])

        if mediaAtributos > 80:
            print(personaje)


def ejercicio3():
    mediaVelocidad = 0
    contadorVelocidades = 0

    for personaje in personajes:
        mediaVelocidad += personaje["atributos"]["velocidad"]
        contadorVelocidades += 1

    mediaVelocidad /= contadorVelocidades

    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > mediaVelocidad:
            print(personaje)


def ejercicio4():
    for personaje in personajes:
        for tecnica in personaje["tecnicas"]:
            if tecnica == "Big Bang Attack":
                if personaje["atributos"]["fuerza"] <= 90:
                    personaje["atributos"]["fuerza"] += 10
                else:
                    personaje["atributos"]["fuerza"] = 100
                break

        print(personaje["nombre"], personaje["atributos"]["fuerza"])


def ejercicio5():
    fuerza_vegeta = 0

    for vegeta in personajes:
        if vegeta["nombre"] == "Vegeta":
            fuerza_vegeta = vegeta["atributos"]["fuerza"]
            break

    for personaje in personajes:
        if personaje["nombre"] != "Vegeta":
            if personaje["atributos"]["defensa"] < fuerza_vegeta:
                print(personaje["nombre"], personaje["atributos"]["defensa"])


def ejercicio6():
    for personaje in personajes[:]:
        if personaje["raza"] == "Saiyajin":
            personajes.remove(personaje)

    print(personajes)
