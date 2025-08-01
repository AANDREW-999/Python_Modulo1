# bloque2_estructuras_funciones/ejercicio8_palíndromo.py

"""
Ejercicio 8: Validar de palíndromo
Determina si una palabra o frase es un palíndromo, ignorando espacios y mayúsculas.
"""

def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

# Prueba de la función con ejemplos de palabras y frases
print(f"Ejemplo de palíndromos:\n")
ejemplos = [
    "Anita lava la tina",
    "Reconocer",
    "Amo la pacifica paloma",
    "La ruta natural"
]

for ejemplo in ejemplos:
    resultado = es_palindromo(ejemplo)
    if resultado:
        print(f"'{ejemplo}' es un palíndromo.")
    else:
        print(f"'{ejemplo}' no es un palíndromo.")

# Solicitar al usuario una palabra o frase para verificar si es un palíndromo
palabra = input("\nIngrese una palabra o frase: ")

resultado = es_palindromo(palabra)
if resultado:
    print(f"\n\t'{palabra}' es un palíndromo.")
else:
    print(f"\n\t'{palabra}' no es un palíndromo.")


