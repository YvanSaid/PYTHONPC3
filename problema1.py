def obtener_porcentage():
    while True:
        try:
            fraccion = input("Ingrese una fracción (X/Y): ")
            X, Y = map(int, fraccion.split('/'))
            if Y == 0:
                raise ZeroDivisionError
            if X > Y:
                raise ValueError
            porcentage = (X / Y) * 100

            if porcentage < 1:
                return "E"
            elif porcentage > 99:
                return "F"
            else:
                return f"{round(porcentage)}%"
        except ValueError:
            print("Debe ingresar dos números enteros")
        except ZeroDivisionError:
            print("No se puede dividir entre cero")

if __name__ == "__main__":
    print(obtener_porcentage())
