class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
    
    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

if __name__ == "__main__":
    catalogo = Catalogo()
    producto1 = Producto("Filtro de aceite", 50, 2023)
    producto2 = Producto("Batería", 100, 2022)
    producto3 = Producto("Neumático", 80, 2021)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    print("Lista de productos:")
    catalogo.mostrar_productos()

    print("\nProductos del año 2022:")
    productos_2022 = catalogo.filtrar_por_año(2022)
    for producto in productos_2022:
        print(producto)
