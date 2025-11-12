from Utilidades import Mostrar_Titulo, limpiar_Consola, leer_año, nombre_dia, salir
from Calendario import es_bisiesto, dia_1_enero
def main():
    Mostrar_Titulo() # Muestra el título del programa
    limpiar_Consola()
    # Bucle principal del programa
    while True:
        año = leer_año()# Solicita al usuario que ingrese un año válido
        
        if es_bisiesto(año):# Verifica si el año es bisiesto con la función es_bisiesto
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
        
        dia_semana = dia_1_enero(año) # Obtiene el día de la semana del 1 de enero del año ingresado llamando a la función dia_1_enero
        nombre_dia_semana = nombre_dia(dia_semana) # Convierte el número del día de la semana a su nombre correspondiente
        print(f"El 1 de enero de {año} cae en: {nombre_dia_semana}.")
        
        if salir(): # Pregunta al usuario si desea salir del programa
            print("Saliendo del programa. ")
            break
        
        limpiar_Consola() # Limpia la consola antes de la siguiente iteración

if __name__ == "__main__":
    main()