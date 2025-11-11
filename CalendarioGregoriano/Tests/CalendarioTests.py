
import unittest # Importa el módulo unittest para pruebas unitarias
from Calendario import es_bisiesto # Importa la función es_bisiesto desde el módulo Calendario

class TestCalendario(unittest.TestCase): # Clase de pruebas unitarias para el módulo Calendario

    def test_es_bisiesto(self): # Pruebas para la función es_bisiesto   

        self.assertTrue(es_bisiesto(2000))  # Divisible por 400
        self.assertFalse(es_bisiesto(1900)) # Divisible por 100 pero no por 400

        self.assertTrue(es_bisiesto(2012))  # Divisible por 4 pero no por 100
        self.assertFalse(es_bisiesto(2019)) # No es bisiesto

    

