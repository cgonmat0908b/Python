def es_primo(num : int) -> bool:
    contador = 0
    primo = True
    if num == 1:
        primo = False
    else:
        for i in range(2,num):
            if num % i == 0:
                contador += 1
            if contador == 1:
                primo = False
                break
    return primo


def primos_hasta(limite : int) -> tuple:
    # Lista de primos entre 2 y limite
    # Cuantos hay 
    # Suma de todos
    listaPrimos = []
    for i in range(1,limite + 1):
        if es_primo(i):
            listaPrimos.append(i)

    return listaPrimos,len(listaPrimos),sum(listaPrimos)


print(primos_hasta(20))



