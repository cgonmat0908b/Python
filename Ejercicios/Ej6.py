contrasenya = "Desconocida"

while(contrasenya != "12345"):
    contrasenya = input("Introduce la contraseña: ")

    if(contrasenya == "12345"):
        print("Bienvenido.")
    else:
        print("Incorrecto.")