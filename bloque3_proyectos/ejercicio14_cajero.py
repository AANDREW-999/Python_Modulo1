# bloque3_proyectos/ejercicio14_cajero.py

"""
Simulador de Cajero Automático (ATM).
Permite consultar saldo, depositar y retirar dinero.
"""

saldo = 1000.0  # Saldo inicial

def consultar_saldo():
    """
    Muestra el saldo actual.
    """
    print(f"Saldo actual: ${saldo:.2f}")

def depositar():
    """
    Permite depositar dinero en la cuenta.
    """
    global saldo
    try:
        monto = float(input("Ingrese el monto a depositar: "))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return
        saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Monto inválido.")

def retirar():
    """
    Permite retirar dinero de la cuenta si hay saldo suficiente.
    """
    global saldo
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return
        if monto > saldo:
            print("Fondos insuficientes.")
            return
        saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Monto inválido.")

def menu():
    """
    Muestra el menú principal e interactúa con el usuario.
    """
    while True:
        print("\n--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()