def estadisticas(*num) -> list:
    mayor = max(num)
    menor = min(num)
    media = sum(num) / len(num)
    return [mayor,menor,media]


resultado = estadisticas(1,2,3,4,5,5,5,5)

print(resultado[0])
print(resultado[1])
print(resultado[2])
