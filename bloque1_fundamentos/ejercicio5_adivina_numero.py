# bloque1_fundamentos/ejercicio5_adivina_numero.py

"""
Ejercicio 5: Adivina el Número
El programa piensa un número secreto entre 1 y 100.
El usuario debe adivinarlo. Se indica si el intento es mayor o menor.
Conceptos: while, if/elif/else, input(), int(), operadores relacionales.
"""

numero_secreto = 42  # Número secreto definido estáticamente

print("Adivina el número secreto entre 1 y 100.")

while True:
    intento_input = input("Introduce tu intento: ")
    try:
        intento = int(intento_input)
        if intento < 1 or intento > 100:
            print("Error: El número debe estar entre 1 y 100.")
            continue
        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break
    except ValueError:
        print("Error: Debes introducir un número entero.")