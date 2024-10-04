import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

if __name__ == "__main__":
    C1=float(input("Radio del 1er circulo: "))
    circulo1 = Circulo(C1)
    C2=float(input("Radio del 2do circulo: "))
    circulo2 = Circulo(C2)

    print(f"Área del círculo 1: {circulo1.calcular_area()}")
    print(f"Área del círculo 2: {circulo2.calcular_area()}")
