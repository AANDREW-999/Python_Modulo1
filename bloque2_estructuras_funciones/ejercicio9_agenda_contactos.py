# bloque2_estructuras_funciones/ejercicio9_agenda_contactos.py

"""
Ejercicio 9: Agenda de Contactos con Diccionario
Permite añadir, buscar y mostrar contactos usando un diccionario.
"""


def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' añadido.")

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def mostrar_contactos(agenda):
    if agenda:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print("La agenda está vacía.")

agenda = {}

while True:
    print("\nMenú de Agenda de Contactos:")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(agenda, nombre, telefono)
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        buscar_contacto(agenda, nombre)
    elif opcion == "3":
        mostrar_contactos(agenda)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")