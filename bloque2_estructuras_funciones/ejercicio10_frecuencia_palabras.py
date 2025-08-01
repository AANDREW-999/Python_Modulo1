# bloque2_estructuras_funciones/ejercicio10_frecuencia_palabras.py

"""
Ejercicio 10: Contador de Frecuencia de Palabras
Devuelve un diccionario con la frecuencia de cada palabra en un texto.
"""

def contar_frecuencia_palabras(texto):
    texto = texto.lower()
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# Prueba de la función
texto_ejemplo = "Hola mundo hola Python mundo mundo"
print(texto_ejemplo)
resultado = contar_frecuencia_palabras(texto_ejemplo)
print(resultado)

# Solicitar al usuario un texto para contar la frecuencia de palabras
texto_usuario = input("\nIngrese un texto: ")
resultado_usuario = contar_frecuencia_palabras(texto_usuario)
print(resultado_usuario)