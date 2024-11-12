# Sistema de Gestión de Inventario
Este proyecto es un sistema de gestión de inventario básico en Python. Permite agregar, actualizar, eliminar y buscar productos en un inventario. Además, guarda los datos en archivos de texto y mantiene un historial de modificaciones realizadas.

## Estructura del Proyecto

El proyecto está compuesto por tres archivos principales:

1. main.py: El archivo que maneja la lógica principal de la aplicación, donde el usuario puede interactuar con el inventario a través de un menú.

2. inventario.py: Contiene la clase Inventario, que gestiona el almacenamiento y las operaciones relacionadas con los productos.

3. producto.py: Define la clase Producto, que modela un producto con sus atributos (nombre, categoría, precio y cantidad) y proporciona métodos para obtener y modificar estos valores.


# Instalación
Para utilizar el sistema, asegúrate de tener Python instalado en tu máquina. No es necesario instalar ninguna librería externa, ya que todo el proyecto se desarrolla utilizando bibliotecas estándar de Python.

1. Clona este repositorio a tu máquina local:   
git clone https://github.com/luisandresmartinezb/Inventario-python

2. Navega a la carpeta del proyecto:
cd proyecto-inventario

3. Ejecuta el archivo main.py
python main.py


# Funcionalidades

## 1. Menu Principal:
El programa proporciona un menú interactivo que permite al usuario realizar diversas operaciones sobre el inventario:

- **Agregar Producto**: Permite agregar un nuevo producto al inventario.
- **Actualizar producto**: Permite actualizar el precio o la cantidad de un producto existente.
- **Eliminar producto**: Permite eliminar un producto del inventario.
- **Mostrar inventario**: Muestra todos los productos actuales en el inventario.
- **Buscar producto**: Permite buscar un producto por su nombre.
- **Salir**: Sale del programa.

## 2. Estructura de las Clases
**2.1 Clase**: Producto (producto.py)
La clase Producto representa un producto en el inventario. Sus atributos son:
- **nombre** : nombre del producto.
- **categoria** : categoría del producto (por ejemplo, "Electrónica", "Ropa").
- **precio** : precio del producto, validado para ser un número mayor que 0.
- **cantidad** : cantidad del producto disponible, validada para ser mayor o igual que 0.

**Métodos principales**:
- **Getters** : get_nombre(), get_categoria(), get_precio(), get_cantidad()
- **Setters**: set_precio(), set_cantidad() (ambos con validaciones).
- **Método** : __str__(): Devuelve una representación en cadena del producto.

**2.2 Clase** : Inventario (inventario.py)
La clase Inventario maneja la gestión de los productos. Utiliza archivos de texto para guardar el inventario y el historial de modificaciones. Sus atributos son:
-**archivo** : El archivo de texto donde se guarda el inventario.
-**archivo_old**: El archivo de texto donde se registra el historial de cambios.

**Métodos principales**:
- **verificar_archivos()** : Crea los archivos necesarios si no existen. 
- **cargar_inventario()** : Carga los productos desde el archivo de inventario.
- **guardar_inventario()** : Guarda el inventario actual en el archivo.
- **registrar_historial()** : Registra los cambios realizados (producto agregado, actualizado o eliminado) en el archivo .old.txt.
- **agregar_producto()** : Agrega un nuevo producto al inventario.
- **actualizar_producto()** : Actualiza el precio o la cantidad de un producto existente
- **eliminar_producto()** : Elimina un producto del inventario.
- **mostrar_inventario()** : Muestra todos los productos en el inventario
- **buscar_producto()** : Busca un producto por su nombre

**3.1 Clase**: main (main.py)
El archivo main.py contiene la lógica de ejecución principal:

1 - **pedir_dato()**: Función auxiliar para pedir datos al usuario y validarlos.
2 - **main()** : La función que ejecuta el menú y las operaciones del inventario
3- **agregar_producto(), actualizar_producto(), eliminar_producto(), buscar_producto()** : Funciones auxiliares que se ejecutan según la opción seleccionada en el menú.

# Archivos

- **registro_inventario.txt**: Archivo donde se guarda el inventario actual.
- **registro_inventario.old.txt:** : Archivo donde se guarda el historial de productos eliminados o modificados.

# Ejemplo de Uso

1. Ejecuta el programa y selecciona una opción del menú:

--- MENÚ DE INVENTARIO ---
1. Agregar producto
2. Actualizar producto
3. Eliminar producto
4. Mostrar inventario
5. Buscar producto
6. Salir

- **Si** eliges agregar un producto, el programa pedirá los detalles del producto, como el nombre, categoría, precio y cantidad.
- **Si** eliges actualizar un producto, el programa te pedirá el nombre del producto y, opcionalmente, puedes actualizar el precio o la cantidad.
- **Si** eliges eliminar un producto, el programa pedirá el nombre del producto a eliminar.
- **Si** eliges mostrar el inventario, se mostrará una lista de todos los productos actuales.

# Contribución: 
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request con tus cambios.

# Licencia 
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.




   
