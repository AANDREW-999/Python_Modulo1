# bloque2_estructuras_funciones/ejercicio6_calificaciones.py

"""
Ejercicio 6: Calificaciones de Estudiantes
Calcula el promedio, la calificación más alta y la más baja de una lista.
"""

def analizar_calificaciones(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    mayor = max(calificaciones)
    menor = min(calificaciones)
    return promedio, mayor, menor

# Prueba de la función con una lista de calificaciones
Lista = [85, 90, 78, 92, 88, 76, 95, 89]
print(Lista)
resultado = analizar_calificaciones(Lista)
print(f"Promedio: {resultado[0]:.2f}")
print(f"Calificación más alta: {resultado[1]}")
print(f"Calificación más baja: {resultado[2]}")


