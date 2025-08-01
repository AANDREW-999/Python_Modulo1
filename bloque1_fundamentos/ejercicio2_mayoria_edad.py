# bloque1_fundamentos/ejercicio2_mayoria_edad.py

"""
Ejercicio 2: Verificador de Mayoría de Edad
Solicita la edad del usuario y muestra si es mayor de edad.
"""

edad_input = input("Introduce tu edad: ")

if not edad_input.isdigit():
    print("Error: Solo se aceptan números.")
else:
    edad = int(edad_input)
    if edad >= 18:
        print("Eres mayor de edad.")
        if 18 <= edad <= 25:
            print("Eres un joven adulto.")
    else:
        print("Eres menor de edad.")