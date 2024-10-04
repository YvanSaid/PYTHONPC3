def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Tipo de dato no válido."
    return a + b

def resta(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Tipo de dato no válido."
    return a - b

def producto(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Tipo de dato no válido."
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No es posible dividir entre cero."
    except TypeError:
        return "Tipo de dato no válido." 

