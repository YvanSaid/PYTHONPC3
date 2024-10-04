from problema3 import Circulo
from problema4 import Rectangulo, Cuadrado

def menu():
    while True:
        print("\n1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"Área del círculo: {circulo.calcular_area()}")
        
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.calcular_area()}")
        
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"Área del cuadrado: {cuadrado.calcular_area()}")
        
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
