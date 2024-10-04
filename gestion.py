class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                print(libro)

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontró ningún libro con el título '{titulo}'.")

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontró ningún libro del autor '{autor}'.")
