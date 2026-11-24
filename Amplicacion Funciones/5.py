alumnos = [
    ["Ana",8],
    ["Paco",7],
    ["Enrique",10],
    ["Maria",1]
]

def filtrar_notas(alumnos : list, nota : float = 5):
    listaResuelta = []
    for alum in alumnos:
        if alum[1] >= nota:
            listaResuelta.append(alum[0])

    return sorted(listaResuelta)


print(filtrar_notas(alumnos))
