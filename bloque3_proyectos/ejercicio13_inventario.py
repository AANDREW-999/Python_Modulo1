# bloque3_proyectos/ejercicio13_inventario.py

"""
Mini Sistema de Gestión de Inventario de una tienda.
Permite agregar productos, realizar ventas y mostrar el inventario.
"""

inventario = []

def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    """
    nombre = input("Nombre del producto: ").strip()
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad en stock: "))
    except ValueError:
        print("Precio o cantidad inválidos.")
        return
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.")

def realizar_venta():
    """
    Realiza la venta de un producto y actualiza la cantidad en el inventario.
    """
    nombre = input("Nombre del producto a vender: ").strip()
    try:
        cantidad_venta = int(input("Cantidad a vender: "))
    except ValueError:
        print("Cantidad inválida.")
        return
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_venta:
                producto["cantidad"] -= cantidad_venta
                total = producto["precio"] * cantidad_venta
                print(f"Venta realizada. Total: ${total:.2f}")
            else:
                print("No hay suficiente stock.")
            return
    print("Producto no encontrado.")

def mostrar_inventario():
    """
    Muestra todos los productos en el inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario actual:")
    for producto in inventario:
        print(f"- {producto['nombre']}: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

def menu():
    """
    Muestra el menú principal e interactúa con el usuario.
    """
    while True:
        print("\n--- Menú Inventario ---")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()