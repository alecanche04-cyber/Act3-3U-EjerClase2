def nombre_dia(numero): # Devuelve el nombre del día de la semana dado su número (1-7)
    
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero, "Número de día inválido") # Retorna un mensaje si el número no es válido

def año_valido(año): # Verifica si un año es válido (mayor que 1582)
    return año > 1582 # El calendario gregoriano comenzó en 1582

def leer_año(): # Solicita al usuario que ingrese un año válido
    while True:
        try:
            año = int(input("Ingrese un año (mayor que 1582): "))
            if año_valido(año):
                return año
            else:
                print("Año inválido. Por favor, ingrese un año mayor que 1582.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")



