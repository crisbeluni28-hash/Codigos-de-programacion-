class Empleado:
    def __init__(self, Nombre, Salario_Base):
        self.Nombre = Nombre
        self.Salario_Base = Salario_Base

    def Calcular_Salario(self):
        return self.Salario_Base

class Gerente(Empleado):
    def __init__(self, Nombre, Salario_Base):
        super().__init__(Nombre, Salario_Base)

    def Calcular_Salario(self):
        return self.Salario_Base + (self.Salario_Base * 0.30)

class Vendedor(Empleado):
    def __init__(self, Nombre, Salario_Base, Ventas):
        super().__init__(Nombre, Salario_Base)
        self.Ventas = Ventas

    def Calcular_Salario(self):
        return self.Salario_Base + (self.Ventas * 0.10)


empleado = Empleado("Oriana", 10000)
gerente = Gerente("Franklin", 20000)
vendedor = Vendedor("Christhofer", 1200, 5000)

Trabajadores = [empleado, gerente, vendedor]

for Trabajador in Trabajadores:

  print(
      f"El trabajador {Trabajador.Nombre} ({type(Trabajador).__name__}) gana:"
      f" ${Trabajador.Calcular_Salario():.2f} de sueldo"
  )