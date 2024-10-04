class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    R1=float(input("Largo del rectangulo: "))
    R2=float(input("Ancho del rectangulo: "))
    rectangulo = Rectangulo(R1, R2)
    R3=float(input("Lado del cuadrado: "))
    cuadrado = Cuadrado(R3)

    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
