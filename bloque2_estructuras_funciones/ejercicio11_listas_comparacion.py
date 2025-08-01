# bloque2_estructuras_funciones/ejercicio11_listas_comparacion.py

"""
Ejercicio 11: Elementos Comunes y Únicos entre Listas
Devuelve conjuntos con elementos comunes y únicos entre dos listas.
"""

def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    comunes = set1 & set2
    solo_lista1 = set1 - set2
    solo_lista2 = set2 - set1
    return (comunes, solo_lista1, solo_lista2)

# Prueba de la función
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7]
print(l1)
print(l2)
resultado = comparar_listas(l1, l2)
print("Comunes:", resultado[0])
print("Solo en lista 1:", resultado[1])
print("Solo en lista 2:", resultado[2])