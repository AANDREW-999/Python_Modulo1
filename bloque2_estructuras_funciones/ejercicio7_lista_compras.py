# bloque2_estructuras_funciones/ejercicio7_lista_compras.py

"""
 Ejercicio 7: Lista de Compras Interactiva
 Permite al usuario agregar, eliminar y ver items en una lista de compras.
"""

lista_compras = []

while True:
    print("\nLista de Compras:")
    print("1. Agregar item")
    print("2. Eliminar item")
    print("3. Ver lista")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        item = input("Ingresa el nombre del item a agregar: ")
        lista_compras.append(item)
        print(f"'{item}' ha sido agregado a la lista.")

    elif opcion == '2':
        item = input("Ingresa el nombre del item a eliminar: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' ha sido eliminado de la lista.")
        else:
            print(f"'{item}' no se encuentra en la lista.")

    elif opcion == '3':
        if lista_compras:
            print("Items en la lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("La lista de compras está vacía.")

    elif opcion == '4':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida, por favor intenta de nuevo.")