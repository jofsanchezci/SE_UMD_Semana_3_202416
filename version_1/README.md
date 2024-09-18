
# Sistema Experto Basado en Reglas en Python

Este proyecto es una implementación básica de un sistema experto basado en reglas en Python. Este sistema puede hacer diagnósticos simples sobre problemas de automóviles usando hechos y reglas para emitir recomendaciones.

## Descripción del Sistema

El sistema está diseñado en torno a una base de conocimiento que contiene hechos y reglas. Las reglas siguen la estructura SI (condición) ENTONCES (acción), y cuando una condición es verdadera, el sistema ejecuta la acción correspondiente.

### Componentes Principales:

1. **BaseDeConocimiento**: Clase que almacena hechos y reglas. 
    - Los **hechos** representan información objetiva sobre el estado del sistema.
    - Las **reglas** relacionan condiciones con acciones que deben ejecutarse si se cumplen las condiciones.

2. **Regla**: Cada regla tiene una condición y una acción. La condición es evaluada contra los hechos, y si es verdadera, la acción es ejecutada.

### Encadenamiento hacia adelante:
Este sistema usa **encadenamiento hacia adelante**, lo que significa que parte de los hechos iniciales y, mediante la evaluación de reglas, deriva nuevas conclusiones o recomendaciones.

## Ejemplo de uso:

### Código:

```python
# Base de hechos y reglas
class BaseDeConocimiento:
    def __init__(self):
        # La base de conocimiento tiene hechos y reglas
        self.hechos = {}
        self.reglas = []
    
    # Método para agregar hechos
    def agregar_hecho(self, clave, valor):
        self.hechos[clave] = valor
    
    # Método para agregar reglas
    def agregar_regla(self, regla):
        self.reglas.append(regla)
    
    # Método para aplicar las reglas y generar recomendaciones
    def aplicar_reglas(self):
        print("\nAplicando reglas para diagnosticar el problema...\n")
        for regla in self.reglas:
            regla.aplicar(self.hechos)

# Clase que define una regla en formato SI (condición) ENTONCES (acción)
class Regla:
    def __init__(self, condicion, accion):
        self.condicion = condicion  # Función que evalúa la condición
        self.accion = accion        # Función que se ejecuta si se cumple la condición
    
    # Método que evalúa y ejecuta la regla
    def aplicar(self, hechos):
        if self.condicion(hechos):
            self.accion(hechos)

# Funciones que actúan como condiciones y acciones
def condicion_bateria_muerta(hechos):
    return hechos.get('auto_no_arranca') and hechos.get('luces_no_se_encieden')

def accion_bateria_muerta(hechos):
    print("Recomendación: La batería del automóvil parece estar muerta. Intenta reemplazarla o recargarla.")

def condicion_sin_gasolina(hechos):
    return hechos.get('auto_no_arranca') and hechos.get('tanque_vacio')

def accion_sin_gasolina(hechos):
    print("Recomendación: El automóvil parece estar sin gasolina. Llena el tanque y vuelve a intentarlo.")

def condicion_arranca_pero_falla(hechos):
    return hechos.get('auto_arranca') and hechos.get('motor_falla')

def accion_arranca_pero_falla(hechos):
    print("Recomendación: El motor del automóvil parece tener un problema. Revisa el sistema de inyección de combustible o las bujías.")

# Ejemplo de uso del sistema experto

# Crear una instancia de la base de conocimiento
base_de_conocimiento = BaseDeConocimiento()

# Agregar hechos (datos sobre el estado actual del automóvil)
base_de_conocimiento.agregar_hecho('auto_no_arranca', True)
base_de_conocimiento.agregar_hecho('luces_no_se_encieden', True)
base_de_conocimiento.agregar_hecho('tanque_vacio', False)
base_de_conocimiento.agregar_hecho('auto_arranca', False)
base_de_conocimiento.agregar_hecho('motor_falla', False)

# Agregar reglas a la base de conocimiento
base_de_conocimiento.agregar_regla(Regla(condicion_bateria_muerta, accion_bateria_muerta))
base_de_conocimiento.agregar_regla(Regla(condicion_sin_gasolina, accion_sin_gasolina))
base_de_conocimiento.agregar_regla(Regla(condicion_arranca_pero_falla, accion_arranca_pero_falla))

# Aplicar las reglas para diagnosticar el problema
base_de_conocimiento.aplicar_reglas()
```

### Salida Esperada:

El sistema diagnosticará el problema y recomendará la acción adecuada con base en los hechos proporcionados.

```plaintext
Aplicando reglas para diagnosticar el problema...

Recomendación: La batería del automóvil parece estar muerta. Intenta reemplazarla o recargarla.
```

## Requerimientos

- Python 3.x

## Cómo Ejecutar

1. Clonar el repositorio o descargar el código.
2. Ejecutar el script de Python en un entorno con Python 3.x instalado.

```bash
python BaseK.py
```

## Expansión del Sistema

Puedes añadir más reglas y hechos para hacer que el sistema sea más completo, adaptándolo a otros dominios de conocimiento como medicina, finanzas, entre otros.
