milimetrosLluvia = (int)(input("Cuantos milimetros de lluvia han caido:"))

if(milimetrosLluvia < 60):
    print("No hay alerta")
elif(milimetrosLluvia >= 60 and milimetrosLluvia < 120):
    print("Hay alerta amarailla")
else:
    print("Hay alerta roja")


match milimetrosLluvia:
    case i if i < 60:
        print("No hay alerta")

    case i if i > 60 and i < 120:
        print("Hay alerta amarilla")

    case i if i >= 120:
        print("Hay alerta roja")