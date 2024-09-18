
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
