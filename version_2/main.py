
import sys
from sistema_experto import BaseDeConocimiento, Regla, condicion_bateria_muerta, accion_bateria_muerta, condicion_sin_gasolina, accion_sin_gasolina, condicion_arranca_pero_falla, accion_arranca_pero_falla

# Función para leer los hechos desde un archivo de pruebas
def cargar_hechos_desde_archivo(ruta_archivo):
    hechos = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if "=" in linea:
                clave, valor = linea.strip().split('=')
                hechos[clave] = valor == 'True'
    return hechos

# Función main que llama al sistema experto con los hechos cargados
def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo_pruebas>")
        sys.exit(1)

    archivo_pruebas = sys.argv[1]

    # Cargar hechos desde el archivo
    hechos = cargar_hechos_desde_archivo(archivo_pruebas)

    # Crear una instancia de la base de conocimiento
    base_de_conocimiento = BaseDeConocimiento()

    # Agregar reglas a la base de conocimiento
    base_de_conocimiento.agregar_regla(Regla(condicion_bateria_muerta, accion_bateria_muerta))
    base_de_conocimiento.agregar_regla(Regla(condicion_sin_gasolina, accion_sin_gasolina))
    base_de_conocimiento.agregar_regla(Regla(condicion_arranca_pero_falla, accion_arranca_pero_falla))

    # Agregar hechos al sistema
    for clave, valor in hechos.items():
        base_de_conocimiento.agregar_hecho(clave, valor)

    # Aplicar las reglas y diagnosticar el problema
    base_de_conocimiento.aplicar_reglas()

# Ejecutar la función main si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
