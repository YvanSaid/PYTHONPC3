def notas():
    while True:
        try:
            calificacion = input("Ingrese una lista de calificaciones separadas por comas: ").split(',')
            calificacion = [int(calif.strip()) for calif in calificacion]
            return calificacion
        except ValueError:
            print("Asegúrese de ingresar solo números enteros separados por comas.")

if __name__ == "__main__":
    print(notas())
