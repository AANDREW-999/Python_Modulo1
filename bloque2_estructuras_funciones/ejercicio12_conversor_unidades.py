# bloque2_estructuras_funciones/ejercicio12_conversor_unidades.py

"""
Ejercicio 12: Conversor de Unidades
Convierte cantidades entre diferentes unidades usando factores de conversión.
"""

factores_conversion = {
    ("metros", "pies"): 3.28084,
    ("pies", "metros"): 0.3048,
    ("kilometros", "millas"): 0.621371,
    ("millas", "kilometros"): 1.60934,
    ("centimetros", "pulgadas"): 0.393701,
    ("pulgadas", "centimetros"): 2.54
}

def convertir_unidades(cantidad, unidad_origen, unidad_destino):
    clave = (unidad_origen, unidad_destino)
    if clave in factores_conversion:
        return cantidad * factores_conversion[clave]
    else:
        print(f"Conversión de '{unidad_origen}' a '{unidad_destino}' no disponible.")
        return None

# Ejemplo de uso
cantidad = 10
origen = "metros"
destino = "pies"
resultado = convertir_unidades(cantidad, origen, destino)
if resultado is not None:
    print(f"{cantidad} {origen} son {resultado:.2f} {destino}\n")

# Moatrar conversiones y unidades disponibles
unidades_disponibles = ["metros con pies", "pies con metros", "kilometros con millas", "millas con kilometros", "centimetros con pulgadas", "pulgadas con centimetros"]
print("Unidades disponibles para conversión:")
for unidad in unidades_disponibles:
    print(f"- {unidad}")


# Solicitar al usuario una conversión
cantidad_usuario = float(input("\nIngrese la cantidad a convertir: "))
unidad_origen_usuario = input("Ingrese la unidad de origen: ").lower()
unidad_destino_usuario = input("Ingrese la unidad de destino: ").lower()
resultado_usuario = convertir_unidades(cantidad_usuario, unidad_origen_usuario, unidad_destino_usuario)
if resultado_usuario is not None:
    print(f"\n{cantidad_usuario} {unidad_origen_usuario} son {resultado_usuario:.2f} {unidad_destino_usuario}")
