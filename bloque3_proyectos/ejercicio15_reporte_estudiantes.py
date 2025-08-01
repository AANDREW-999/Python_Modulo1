# bloque3_proyectos/ejercicio15_reporte_estudiantes.py

"""
Generador de Reportes de Estudiantes.
Calcula promedios, estados y muestra un reporte formateado.
"""

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    :param calificaciones: lista de números (float o int)
    :return: promedio (float)
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def obtener_estado(promedio):
    """
    Determina el estado del estudiante según el promedio.
    :param promedio: número (float)
    :return: 'Aprobado' o 'Reprobado' (str)
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"

def generar_reporte(estudiantes):
    """
    Genera e imprime el reporte de calificaciones de los estudiantes.
    :param estudiantes: diccionario {nombre: [calificaciones]}
    :return: None
    """
    print("Reporte de Calificaciones:")
    print("-------------------------")
    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.1f}, Estado: {estado}")
    print("-------------------------")

if __name__ == "__main__":
    # Diccionario de ejemplo
    estudiantes = {
        "Ana": [4.5, 4.0, 5.0],
        "Juan": [2.8, 3.0, 2.6],
        "Luis": [3.2, 3.5, 3.0]
    }
    generar_reporte(estudiantes)