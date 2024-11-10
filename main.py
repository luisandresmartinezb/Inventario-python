# main.py
import re  # Importa la librería 're' para trabajar con expresiones regulares.
from producto import Producto  # Importa la clase 'Producto' desde el archivo 'producto.py'.
from inventario import Inventario  # Importa la clase 'Inventario' desde el archivo 'inventario.py'.


# Función para pedir datos al usuario con validación del tipo de entrada.
def pedir_dato(mensaje, tipo):
    while True:
        entrada = input(mensaje)  # Solicita la entrada al usuario.

        # Remover símbolos de moneda (€ o $) y espacios en blanco.
        entrada = re.sub(r'[€$]', '', entrada).strip()

        try:
            return tipo(entrada)  # Intenta convertir la entrada al tipo deseado (float, int, etc.).
        except ValueError:
            print("Entrada no válida, intente de nuevo.")  # Si la conversión falla, muestra un mensaje de error.


# Función principal que maneja la lógica del programa.
def main():
    inventario = Inventario(
        "registro_inventario.txt")  # Crea una instancia de 'Inventario' usando el archivo 'registro_inventario.txt'.

    # Diccionario de opciones para el menú (simulación de switch).
    opciones = {
        "1": lambda: agregar_producto(inventario),  # Agregar un producto al inventario.
        "2": lambda: actualizar_producto(inventario),  # Actualizar la información de un producto.
        "3": lambda: eliminar_producto(inventario),  # Eliminar un producto del inventario.
        "4": lambda: inventario.mostrar_inventario(),  # Mostrar el inventario completo
        "5": lambda: buscar_producto(inventario),  # Buscar un producto por nombre.
        "6": lambda: print("Saliendo del programa.")  # Salir del programa.
    }

    while True:
        # Imprime el menú de opciones en pantalla.
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Elija una opción: ")  # Solicita al usuario que elija una opción del menú.
        accion = opciones.get(opcion)  # Busca la acción correspondiente a la opción seleccionada.

        if accion:
            accion()  # Ejecuta la acción seleccionada.
            if opcion == "6":  # Si el usuario elige salir, se rompe el bucle.
                break
        else:
            print("Opción no válida. Intente nuevamente.")  # Si la opción no es válida, muestra un mensaje de error.


# Función para agregar un nuevo producto al inventario.
def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")  # Solicita el nombre del producto.
    categoria = input("Ingrese la categoría del producto: ")  # Solicita la categoría del producto.
    precio = pedir_dato("Ingrese el precio del producto (puede incluir € o $): ",
                        float)  # Solicita el precio y lo convierte a float.
    cantidad = pedir_dato("Ingrese la cantidad del producto: ", int)  # Solicita la cantidad y la convierte a int.
    producto = Producto(nombre, categoria, precio,
                        cantidad)  # Crea una instancia del producto con los datos proporcionados.
    inventario.agregar_producto(producto)  # Agrega el producto al inventario.


# Función para actualizar la información de un producto en el inventario.
def actualizar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")  # Solicita el nombre del producto.

    # Si el usuario elige actualizar el precio, solicita el nuevo precio.
    nuevo_precio = pedir_dato("Ingrese el nuevo precio (puede incluir € o $, deje vacío para no cambiar): ",
                              float) if input("¿Actualizar precio? (s/n): ").lower() == "s" else None
    # Si el usuario elige actualizar la cantidad, solicita la nueva cantidad.
    nueva_cantidad = pedir_dato("Ingrese la nueva cantidad (deje vacío para no cambiar): ", int) if input(
        "¿Actualizar cantidad? (s/n): ").lower() == "s" else None

    # Llama a la función para actualizar el producto en el inventario.
    inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)


# Función para eliminar un producto del inventario.
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")  # Solicita el nombre del producto a eliminar.
    inventario.eliminar_producto(nombre)  # Llama a la función para eliminar el producto del inventario.


# Función para buscar un producto por su nombre.
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")  # Solicita el nombre del producto.
    inventario.buscar_producto(nombre)  # Llama a la función para buscar el producto en el inventario.


# Ejecuta la función principal si el script se ejecuta directamente.
if __name__ == "__main__":
    main()
