# Clase ABSTRACTA
from abc import ABC,abstractmethod
import math

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

class Triangulo(FiguraGeometrica):
    
    def __init__(self,base,altura):
        
        if base <= 0 or altura <= 0:
            raise ValueError("Valores invalidos introducidos")

        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura / 2)
        
    def perimetro(self):
        return self.base * 3
        
    def __str__(self):
        return f"Triangulo [Base = {self.base} | Triangulo = {self.altura}]"

class Circulo(FiguraGeometrica):
    
    def __init__(self,radio):

        if radio <= 0:
            raise ValueError("Valor invalido")

        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo [Radio = {self.radio}]"

triangulo = Triangulo(5,5)
print(triangulo)

print(triangulo.area())
print(triangulo.perimetro())

circulo = Circulo(5)
print(circulo)

print(circulo.area())
print(circulo.perimetro())
