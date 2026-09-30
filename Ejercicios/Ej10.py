num1 = (int)(input("Introduce un número: "))
num2 = (int)(input("Introduce otro número: "))
contadorDivisibles = 0
primos = 0

if(num1 > num2):
    print("Error")
else:
    for i in range(num2,num1,-1):
        for f in range(i, num1, -1):
            if(f % i == 0):
                contadorDivisibles += 1

            if(contadorDivisibles > 2):
                break
            else:
                primos = f
                
