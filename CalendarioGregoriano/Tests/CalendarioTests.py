
import unittest # Importa el módulo unittest para pruebas unitarias
from Calendario import es_bisiesto # Importa la función es_bisiesto desde el módulo Calendario
from Calendario import dia_1_enero # Importa la función dia_1_enero desde el módulo Calendario

class TestCalendario(unittest.TestCase): # Clase de pruebas unitarias para el módulo Calendario

    def test_es_bisiesto(self): # Pruebas para la función es_bisiesto   

        self.assertTrue(es_bisiesto(2000))  # Divisible por 400
        self.assertFalse(es_bisiesto(1900)) # Divisible por 100 pero no por 400

        self.assertTrue(es_bisiesto(2024))  # Divisible por 4 pero no por 100
        self.assertFalse(es_bisiesto(2023)) # No es bisiesto

    def test_dia_1_enero(self): # Pruebas para la función dia_1_mes

        # Sabemos que el 1 de enero de 1996 fue lunes (1)
        #pruebas para varios años consecutivos
        self.assertEqual(dia_1_enero(1995), 0) # Domingo
        self.assertEqual(dia_1_enero(1996), 1) # Lunes
        self.assertEqual(dia_1_enero(1997), 2) # Martes
        self.assertEqual(dia_1_enero(1998), 4) # Jueves
        self.assertEqual(dia_1_enero(1999), 5) # Viernes
        self.assertEqual(dia_1_enero(2000), 6) # Sábado

        #prueba de años recientes
        self.assertEqual(dia_1_enero(2020), 3) # Miércoles
        self.assertEqual(dia_1_enero(2023), 0) # Domingo
        self.assertEqual(dia_1_enero(2024), 1) # Lunes
        self.assertEqual(dia_1_enero(2025), 3) # Miércoles       