import math
class Figura:
    def area(self):
        return 0
      
class Rectangulo(Figura):
    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura

    def area(self):
        return self.Base * self.Altura

class Circulo(Figura):
    def __init__(self, Radio):
        self.Radio = Radio

    def area(self):
        return math.pi * (self.Radio ** 2)

class Triangulo(Figura):
    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura

    def area(self):
        return (self.Base * self.Altura) / 2


rectangulo = Rectangulo(10, 15)     
circulo = Circulo(7)             
triangulo = Triangulo(5, 6)         

Figuras = [rectangulo, circulo, triangulo]

for Figura in Figuras:
  
    print(f"El área de la figura geometrica {type(Figura).__name__} es de: {Figura.area():.2f} cm")