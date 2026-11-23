class CuentaBancaria:
    #SELF = this en java
    def __init__(self, nombre : str, saldo : float = 0):
        
        if saldo < 0:
            raise ValueError("Saldo negativo invalido")
        
        self.nombre = nombre
        self.saldo = saldo

    def ingresar(self, cantidadIngresar : float):
        if cantidadIngresar < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.saldo +=  cantidadIngresar

    def retirar(self,cantidadRetirar : float):
        if cantidadRetirar > self.saldo or cantidadRetirar < 0:
            raise ValueError("La cantidad no puede ser negativa o superior al saldo")

        self.saldo -= cantidadRetirar

    def __str__(self):
        return f"Cuenta bancaria [Nombre = {self.nombre} | Saldo = {self.saldo}]"

# Inicialización de 2 objetos de la clase cuenta bancaria
cuenta1 = CuentaBancaria("Juan")
cuenta2 = CuentaBancaria("Paco", 2000)

# Mostrar los valores de las cuentas bancarias
print(cuenta1)
print(cuenta2)

# Ingresar 5000€ en la cuenta bancaria 2
cuenta2.ingresar(5000)
print(cuenta2)

# Retirar 5000€ en la cuenta bancaria 2
cuenta2.retirar(5000)
print(cuenta2)

# Ingresar cantidad invalida
cuenta2.ingresar(-500)

# Retirar cantidad invalida
cuenta2.retirar(8000)

# Clase ABSTRACTA
from abc import ABC,abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    
    def __init__(self,base,altura):

        if base <= 0 or altura <= 0:
            raise ValueError("Los valores no pueden ser 0 o menor")
        
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2

    def __str__(self):
        return f"Rectangulo [Base = {self.base} | Altura = {self.altura}]"


r = Rectangulo(1,1)
print(r.perimetro())