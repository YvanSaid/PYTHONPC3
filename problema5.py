class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}, Edad: {self.edad}, Nota: {self.nota}")
    
    def set_age(self, edad):
        self.edad = edad
    
    def set_nota(self, nota):
        self.nota = nota

if __name__ == "__main__":
    Nombre=input("Ingrese el nombre del alumno: ")
    Registro=input("Ingrese el registro del alumno: ")
    alumno = Alumno(Nombre, Registro)
    Edad=input("Ingrese la edad del alumno: ")
    alumno.set_age(Edad)
    Nota=input("Ingrese la nota del alumno: ")
    alumno.set_nota(Nota)
    alumno.display()
