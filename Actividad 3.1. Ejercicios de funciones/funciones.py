# Función con tipos de datos
def sumatorio(num : int) -> int:
    sumatorio = 0
    for i in range(1,num + 1):
        sumatorio += i
    return sumatorio

print(sumatorio(3))

# Función con *, indica que como parametro le entra un número indefinido de valores
def suma(*nums):
    return sum(nums)

print(suma(1,2,3,4))

# Función que tiene varios returns
def suma2(a,b):
    return a+b,a,b

a, b, c = suma2(1,2)

print(a, b, c)
