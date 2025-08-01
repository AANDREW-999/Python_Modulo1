# bloque1_fundamentos/ejercicio3_vocales_consonantes.py

"""
Ejercicio 3: Contador de Vocales y Consonantes
Este programa solicita una frase al usuario, válida que solo contenga letras (sin números ni símbolos),
y cuenta cuántas vocales y consonantes tiene.
-.lower(): Convierte todos los caracteres de una cadena a minúsculas.
-.isalpha(): Verifica si un carácter o cadena contiene solo letras del alfabeto.
"""

frase = input("Introduce una frase (solo letras, sin números ni símbolos): ").replace(" ", "")

if not frase.isalpha():
    print("Error: Solo se aceptan letras. No se permiten números ni caracteres especiales.")
else:
    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0

    for caracter in frase.lower():
        if caracter in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1

    print(f"Número de vocales: {contador_vocales}")
    print(f"Número de consonantes: {contador_consonantes}")
