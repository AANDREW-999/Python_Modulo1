# bloque1_fundamentos/ejercicio4_tabla_multiplicar.py

"""
Ejercicio 4: Tabla de Multiplicar
Solicita un número entero y muestra su tabla de multiplicar del 1 al 10.
Conceptos: input(), int(), bucle for con range(), f-strings.
"""

numero_input = input("Introduce un número entero: ")

try:
    numero = int(numero_input)
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except ValueError:
    print("Error: Debes introducir un número entero.")