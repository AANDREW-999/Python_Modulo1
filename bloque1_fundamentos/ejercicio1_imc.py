# bloque1_fundamentos/ejercicio1_imc.py

"""
Ejercicio 1: Calculadora de Índice de Masa Corporal (IMC)
Calcula el IMC de un usuario con base en su peso y altura.
Válida que los datos ingresados sean numéricos y positivos.
"""

while True:
    peso_input = input("Introduce tu peso en kg: ")
    try:
        peso = float(peso_input)
        if peso > 0:
            break
        else:
            print("Error: El peso debe ser un número positivo.")
    except ValueError:
        print("Error: Solo se aceptan números.")

while True:
    altura_input = input("Introduce tu altura en metros: ")
    try:
        altura = float(altura_input)
        if altura > 0:
            break
        else:
            print("Error: La altura debe ser un número positivo.")
    except ValueError:
        print("Error: Solo se aceptan números.")

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")