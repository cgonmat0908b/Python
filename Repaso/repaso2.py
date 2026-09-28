#Constantes, no existen, así que en mayusculas y ya
PI = 3.14
print(PI)

#Secuencias

#Lista
lista = [1,2,3]
print(lista)
print(lista[0]) #Primer valor
print(lista[-1]) #Ultimo valor
lista[1] = -2 #Cambio de valor de la segunda posición de la lista
lista.append(4) #Añade un valor al final de la lista
lista2 = [1,2,3,4,5,6]
lista.extend(lista2) #Añade a lista, la lista2 desde el último valor de lista
del lista[0] #Borrar el primer elemento de lista

#Tupla

tupla = (1,2,3)
print(tupla)
print(tupla[0])

# Rango
# Puede recibir 3 parametros, Primero : Inicio, Segundo: Fin, Tercero: Salto entre dígito y dígito std(1)
rango = range(1,10)
print(rango)
print(rango[1]) # Segundo valor en el rango

# Tamaño de secuencias
print(len(rango))
print(len(tupla))
print(len(lista))

# Diccionario (Mapa)
diccionario = {
    "Paco" : 32,
    "Pepe" : 48,
    "Juan" : 15
}

print(diccionario)
print(diccionario["Paco"])

# Conjunto ("Hash"), no se pueden repetir los valores
conjunto = {1,2,3,4,5}
print(conjunto)

# Añadir un valor
conjunto.add(7)

# Eliminar
conjunto.remove(2)


# Metodo main
def main():
    print("Hola clase!")

if __name__ == "__main__":
    main()