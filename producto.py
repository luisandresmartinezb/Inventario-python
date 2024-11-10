# producto.py

class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.set_precio(precio)
        self.set_cantidad(cantidad)

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters con validaciones
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self):
        return f"Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"