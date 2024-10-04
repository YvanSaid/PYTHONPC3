#clase punto #REVISARRRRRR
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

if __name__ == "__main__":
    punto1 = Punto(3, 4)
    punto2 = Punto(0, 0)

    print(f"El punto 1 es: {punto1}")
    print(f"El punto 2 es: {punto2}")
    
    print(f"Cuadrante del punto 1: {punto1.cuadrante()}")
    print(f"Cuadrante del punto 2: {punto2.cuadrante()}")

    print(f"Vector entre punto 1 y punto 2: {punto1.vector(punto2)}")
    print(f"Distancia entre punto 1 y punto 2: {punto1.distancia(punto2)}")

#clase rectangulo
class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

if __name__ == "__main__":
    # Crear dos puntos
    punto_inicial = Punto(1, 1)
    punto_final = Punto(4, 5)

    # Crear el rectángulo
    rectangulo = Rectangulo(punto_inicial, punto_final)

    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")
