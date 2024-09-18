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

# Función main que llama al sistema experto
def main():
    # Crear una instancia de la base de conocimiento
    base_de_conocimiento = BaseDeConocimiento()

    # Agregar reglas a la base de conocimiento
    base_de_conocimiento.agregar_regla(Regla(condicion_bateria_muerta, accion_bateria_muerta))
    base_de_conocimiento.agregar_regla(Regla(condicion_sin_gasolina, accion_sin_gasolina))
    base_de_conocimiento.agregar_regla(Regla(condicion_arranca_pero_falla, accion_arranca_pero_falla))

    # Caso 1: La batería está muerta
    print("Ejemplo 1: El automóvil no arranca y las luces no se encienden.")
    base_de_conocimiento.agregar_hecho('auto_no_arranca', True)
    base_de_conocimiento.agregar_hecho('luces_no_se_encieden', True)
    base_de_conocimiento.agregar_hecho('tanque_vacio', False)
    base_de_conocimiento.aplicar_reglas()

    # Limpiar hechos para el siguiente ejemplo
    base_de_conocimiento.hechos.clear()

    # Caso 2: El automóvil no tiene gasolina
    print("\nEjemplo 2: El automóvil no arranca y el tanque está vacío.")
    base_de_conocimiento.agregar_hecho('auto_no_arranca', True)
    base_de_conocimiento.agregar_hecho('luces_no_se_encieden', False)
    base_de_conocimiento.agregar_hecho('tanque_vacio', True)
    base_de_conocimiento.aplicar_reglas()

    # Limpiar hechos para el siguiente ejemplo
    base_de_conocimiento.hechos.clear()

    # Caso 3: El motor falla
    print("\nEjemplo 3: El automóvil arranca, pero el motor falla.")
    base_de_conocimiento.agregar_hecho('auto_arranca', True)
    base_de_conocimiento.agregar_hecho('motor_falla', True)
    base_de_conocimiento.aplicar_reglas()

# Llamar a la función main
if __name__ == "__main__":
    main()
