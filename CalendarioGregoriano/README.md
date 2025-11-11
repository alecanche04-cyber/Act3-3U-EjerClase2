# Act3-3U-EjerClase2
Primera practica de C# en bina, programa que calcula año bisiesto


CalendarioGregoriano/
├── Main.py
├── Calendario.py
├── Utilidades.py
└── Tests/
    └── CalendarioTests.p
    
2. Componentes Principales

📦 Módulo de lógica (calendario.py / Calendario.cs)
Contiene las funciones clave:
- es_bisiesto(año)
- Devuelve True o False según las reglas del calendario gregoriano.
- dia_1_enero(año)
- Calcula el día de la semana del 1 de enero usando como base el año 1996 (lunes).

🧠 Programa principal (main.py / Program.cs)
- Interactúa con el usuario:
- Solicita el año
- Verifica que sea mayor a 1582
- Muestra si es bisiesto
- Muestra el día de la semana con nombre
- Permite salir del programa

🛠️ Utilidades (utils.py / Utils.cs) (opcional)
- Funciones como:
- nombre_dia(numero) → Convierte número (1–7) a nombre del día
- Validaciones de entrada

🧪 Pruebas (tests/test_calendario.py)
- Pruebas unitarias para:
- Años bisiestos conocidos
- Días de la semana esperados
