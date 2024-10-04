#calculos.py
from operaciones import suma, resta, producto, division

if __name__ == "__main__":

    primer=float(input("Ingresa 1er numero: "))
    segundo=float(input("Ingresa 2do numero: "))
    print(suma(primer,segundo))
    print(resta(primer,segundo))
    print(producto(primer,segundo))
    print(division(primer,segundo))
