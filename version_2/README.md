
# Sistema Experto en Python

Este proyecto implementa un sistema experto basado en reglas en Python. El sistema utiliza una base de conocimiento que contiene hechos y reglas. Las reglas siguen el formato SI (condición) ENTONCES (acción) y se aplican a los hechos para proporcionar diagnósticos o recomendaciones.

## Estructura del Proyecto

El proyecto está compuesto por tres archivos principales:

1. **sistema_experto.py**: Contiene la implementación del sistema experto, que incluye la clase `BaseDeConocimiento`, las reglas y sus condiciones.
2. **main.py**: Archivo principal que carga hechos desde un archivo de pruebas y ejecuta el sistema experto.
3. **pruebas.txt**: Archivo de pruebas que contiene diferentes conjuntos de hechos que el sistema experto evaluará.

## Archivos

### sistema_experto.py
Este archivo contiene la implementación básica del sistema experto. Incluye:

- **BaseDeConocimiento**: Clase que almacena hechos y reglas.
- **Regla**: Clase que define las reglas en formato SI (condición) ENTONCES (acción).
- **Funciones de Condiciones y Acciones**: Cada regla tiene una condición que evalúa hechos y una acción que se ejecuta si la condición se cumple.

### main.py
Este archivo carga los hechos desde un archivo de texto pasado como argumento y luego los introduce en el sistema experto, que aplicará las reglas para ofrecer un diagnóstico o recomendación.

### pruebas.txt
Este archivo contiene varios conjuntos de hechos en formato clave-valor que el sistema experto usará para hacer sus evaluaciones.

- **Prueba 1**: El automóvil no arranca y las luces no se encienden (posible batería muerta).
- **Prueba 2**: El automóvil no arranca y el tanque está vacío (posible falta de gasolina).
- **Prueba 3**: El automóvil arranca, pero el motor falla (posible problema del motor).

## Ejecución del Proyecto

Para ejecutar el sistema experto, sigue los siguientes pasos:

1. Clonar o descargar los archivos del proyecto.
2. Ejecutar el archivo `main.py` desde la línea de comandos, pasando como argumento el archivo de pruebas:

```bash
python main.py pruebas.txt
```

## Ejemplo de Salida

```plaintext
Aplicando reglas para diagnosticar el problema...

Recomendación: La batería del automóvil parece estar muerta. Intenta reemplazarla o recargarla.

Aplicando reglas para diagnosticar el problema...

Recomendación: El automóvil parece estar sin gasolina. Llena el tanque y vuelve a intentarlo.

Aplicando reglas para diagnosticar el problema...

Recomendación: El motor del automóvil parece tener un problema. Revisa el sistema de inyección de combustible o las bujías.
```

Cada vez que se ejecuta el programa con un conjunto de hechos, se muestran las recomendaciones basadas en las reglas del sistema experto.

## Expansión del Sistema

Este sistema puede expandirse fácilmente añadiendo nuevas reglas, condiciones y hechos. También puede adaptarse a otros dominios, como medicina, finanzas o cualquier otro campo en el que se necesiten sistemas de toma de decisiones automatizados.
