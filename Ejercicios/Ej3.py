age = (int)(input("Introduce tu edad: "))

if(age < 0):
    print("Error")

elif(age > 120):
    print("Vanpiro esiten")

elif(age >= 0 and age <= 17):
    print("Menor de edad")

else:
    print("Mayor de edad")


