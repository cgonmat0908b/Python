price = (float) (input("Introduce el precio: "))
typeIVA = input("Introduce el tipo de IVA(General, Reducido, Superreducido): ")
total = 0

# Calcular IVA con elif
if(typeIVA == "General"):
    total = price + (price * 0.21)
elif(typeIVA == "Reducido"):
    total = price + (price * 0.10)
else:
    total = price + (price * 0.04)

print("Precio final dado el iva " , typeIVA , ": " , total)

# Calcular IVA con match

match typeIVA:

    case "General":
        total = price + (price * 0.21)

    case "Reducido":
        total = price + (price * 0.10)

    case "Superreducido":
        total = price + (price * 0.04)

print("Precio final dado el iva " , typeIVA , ": " , total)