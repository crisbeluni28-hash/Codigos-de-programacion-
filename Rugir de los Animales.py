class Animal:
    def __init__(self, Edad, Nombre):
        self.Edad = Edad
        self.Nombre = Nombre

    def hacer_sonido(self):
        print("Ruido del animal.")


class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.Nombre} dice: Guau guau! y tiene {self.Edad}")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.Nombre} dice: Miau miau! y tiene {self.Edad}")


class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.Nombre} dice: Muuu y tiene {self.Edad}")

#Valores de prueba 

perro = Perro(14, "Tommy")
gato = Gato(8, "Pelusa")
vaca = Vaca(10, "Licha")

lista_animales = [perro, gato, vaca]

for animal in lista_animales:
    animal.hacer_sonido()