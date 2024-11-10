# inventario.py
from producto import Producto  # Importa la clase Producto para trabajar con objetos de productos
import os  # Importa el módulo os para interactuar con el sistema de archivos

class Inventario:
    def __init__(self, archivo):
        """Inicializa el inventario y define los archivos necesarios."""
        self.__productos = []  # Lista para almacenar los productos del inventario
        self.archivo = archivo  # Nombre del archivo principal de inventario
        self.archivo_old = archivo.replace(".txt", ".old.txt")  # Archivo para registrar productos eliminados o modificados
        self.verificar_archivos()  # Verifica si los archivos existen y los crea si no
        self.cargar_inventario()  # Carga los productos desde el archivo al inicializar el inventario

    def verificar_archivos(self):
        """Crea los archivos si no existen."""
        # Si el archivo de inventario no existe, se crea con un encabezado
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as file:
                file.write("Inventario Actual:\n")
        # Si el archivo de historial de modificaciones no existe, se crea con un encabezado
        if not os.path.exists(self.archivo_old):
            with open(self.archivo_old, "w") as file:
                file.write("Historial de Modificaciones:\n")

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        # Abre el archivo de inventario y lee todas las líneas excepto la primera (encabezado)
        with open(self.archivo, "r") as file:
            lines = file.readlines()[1:]  # Omitir la primera línea de encabezado
            # Procesa cada línea y crea objetos Producto a partir de los datos
            for line in lines:
                nombre, categoria, precio, cantidad = line.strip().split(", ")
                producto = Producto(nombre, categoria, float(precio), int(cantidad))
                self.__productos.append(producto)  # Agrega el producto al inventario

    def guardar_inventario(self):
        """Guarda el inventario actual en el archivo de inventario."""
        # Sobrescribe el archivo de inventario con los productos actuales
        with open(self.archivo, "w") as file:
            file.write("Inventario Actual:\n")
            for producto in self.__productos:
                # Escribe los datos de cada producto en el archivo
                file.write(f"{producto.get_nombre()}, {producto.get_categoria()}, {producto.get_precio()}, {producto.get_cantidad()}\n")

    def registrar_historial(self, mensaje):
        """Registra los productos modificados o eliminados en el archivo .old."""
        # Agrega un mensaje al archivo de historial (archivo .old)
        with open(self.archivo_old, "a") as file:
            file.write(mensaje + "\n")

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario si no existe previamente."""
        # Verifica si el producto ya está en el inventario por su nombre
        if not any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            self.__productos.append(producto)  # Agrega el producto al inventario
            print(f"Producto '{producto.get_nombre()}' agregado al inventario.")
            self.guardar_inventario()  # Guarda el inventario actualizado
        else:
            print(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        """Actualiza un producto existente en el inventario."""
        # Busca el producto por su nombre
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                estado_anterior = str(producto)  # Guarda el estado previo del producto
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)  # Actualiza el precio si se proporciona
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)  # Actualiza la cantidad si se proporciona
                print(f"Producto '{nombre}' actualizado.")

                # Registra la modificación en el archivo de historial
                self.registrar_historial(f"Modificado: Antes: {estado_anterior} | Después: {producto}")

                # Guarda el inventario actualizado
                self.guardar_inventario()
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        # Busca el producto por su nombre
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                # Registra la eliminación en el archivo de historial
                self.registrar_historial(f"Eliminado: {producto}")

                self.__productos.remove(producto)  # Elimina el producto del inventario
                print(f"Producto '{nombre}' eliminado del inventario.")

                # Guarda el inventario actualizado
                self.guardar_inventario()
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            # Imprime cada producto en el inventario
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre):
        """Busca un producto por su nombre."""
        # Busca el producto por su nombre
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                return producto
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        return None
