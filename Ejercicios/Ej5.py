num1 = (int)(input("Introduce un número: "))
num2 = (int)(input("Introduce otro número: "))

# Con for

if(num2 > num1):
    for i in range (num1,num2):
        num1 += 1
        if(num1 % 2 == 0):
            print(num1)

else:
    print("Error, el primer número no puede ser mayor al segundo")


# Con while
num1 = (int)(input("Introduce un número: "))
num2 = (int)(input("Introduce otro número: "))

if(num2 > num1):
    while(num1 != num2):
        num1 += 1
        if(num1 % 2 == 0):
            print(num1)


