def main():
    frutas = ["Manzana", "Pera", "Melocotón"]
    frutas2 = ["Kiwi", "Sandía", "Melón"]

    frutas.extend(frutas2)

    print(frutas[-1])

    tupla = (3,5,6)

    print(tupla[0])

    inicio = int(input("Inicio: "))
    fin = int(input("Fin: "))
    rango = range(inicio,fin)

    print(rango)

    
    
if __name__ == "__main__":
    main()
    