

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): # Una año es bisiesto si es divisible por 4 pero no por 100, o si es divisible por 400
        return True
    else:
        return False
def dia_1_enero(año):
    # Algoritmo de Zeller modificado para calcular el día de la semana del 1 de enero
    q = 1  # Día del mes
    m = 13  # Enero es tratado como el mes 13 del año anterior
    K = (año - 1) % 100  # El año dentro del siglo
    J = (año - 1) // 100  # El siglo

    # Fórmula de Zeller
    f = q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    dia_semana = f % 7 #Sacamos el modulo que va a indicar el dia de la semana
    # Ajustar para que 0 = Domingo, 1 = Lunes, etc...
    dia_semana = (dia_semana + 7) % 7

    return dia_semana