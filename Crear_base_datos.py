import sqlite3
import bcrypt

conn=sqlite3.connect('base_inventario.db')
c=conn.cursor()
import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('empleados.db')
c = conn.cursor()

# Función para crear la tabla de empleados y agregar un empleado
def create_tablePersonal():
    # Crear la tabla de empleados
    c.execute('''CREATE TABLE IF NOT EXISTS personal (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    apellido TEXT, 
                    correo TEXT, 
                    telefono TEXT, 
                    direccion TEXT, 
                    fecha_nacimiento TEXT, 
                    fecha_contratacion TEXT, 
                    puesto TEXT, 
                    username TEXT UNIQUE, 
                    password TEXT)''')
    conn.commit()
    
    # Insertar un empleado de ejemplo
    c.execute("INSERT INTO personal (nombre, apellido, correo, telefono, direccion, fecha_nacimiento, fecha_contratacion, puesto, username, password) "
              "VALUES ('Juan', 'Pérez', 'juan.perez@example.com', '555-1234', 'Calle Ficticia 123', '1990-05-12', '2023-01-15', 'Desarrollador', 'rey', '123')")
    conn.commit()
# create_tablePersonal()
# Función para verificar el nombre de usuario y la contraseña
def verificar_usuario(username, password):
    # Buscar al empleado por su username
    c.execute("SELECT * FROM personal WHERE username = ?", (username,))
    empleado = c.fetchone()
    
    # Si no se encuentra al empleado
    if empleado is None:
        print("Usuario no encontrado.")
        return False
    
    else:
        return True
# verificar_usuario("mfray", "123")
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS inventario(codigo TEXT,producto TEXT ,laboratorio TEXT,cantidad TEXT,precio_und TEXT)")
	conn.commit()
	c.execute("INSERT INTO inventario values ('1f21','Lansoprazol','basico','120','2')")
	c.execute("INSERT INTO inventario VALUES ('001', 'Martillo', 'Herramientas', '50', '15')")
	c.execute("INSERT INTO inventario VALUES ('002', 'Destornillador', 'Herramientas', '100', '5')")
	c.execute("INSERT INTO inventario VALUES ('003', 'Taladro', 'Electrico', '30', '120')")
	c.execute("INSERT INTO inventario VALUES ('004', 'Sierra Circular', 'Electrico', '20', '200')")
	c.execute("INSERT INTO inventario VALUES ('005', 'Llave Inglesa', 'Herramientas', '40', '25')")
	c.execute("INSERT INTO inventario VALUES ('006', 'Alicates', 'Herramientas', '70', '8')")
	c.execute("INSERT INTO inventario VALUES ('007', 'Cinta Métrica', 'Medición', '80', '3')")
	c.execute("INSERT INTO inventario VALUES ('008', 'Clavos 2 pulgadas', 'Fijación', '500', '0.1')")
	c.execute("INSERT INTO inventario VALUES ('009', 'Tornillos M6', 'Fijación', '300', '0.2')")
	c.execute("INSERT INTO inventario VALUES ('010', 'Brocha', 'Pintura', '90', '2')")
	c.execute("INSERT INTO inventario VALUES ('011', 'Rodillo', 'Pintura', '75', '5')")
	c.execute("INSERT INTO inventario VALUES ('012', 'Pintura Blanca', 'Pintura', '60', '12')")
	c.execute("INSERT INTO inventario VALUES ('013', 'Pegamento Epoxi', 'Adhesivos', '40', '10')")
	c.execute("INSERT INTO inventario VALUES ('014', 'Lijas', 'Pulido', '100', '0.5')")
	c.execute("INSERT INTO inventario VALUES ('015', 'Masilla', 'Reparación', '35', '8')")
	c.execute("INSERT INTO inventario VALUES ('016', 'Pala', 'Construcción', '25', '12')")
	c.execute("INSERT INTO inventario VALUES ('017', 'Carretilla', 'Construcción', '10', '50')")
	c.execute("INSERT INTO inventario VALUES ('018', 'Nivel', 'Medición', '15', '10')")
	c.execute("INSERT INTO inventario VALUES ('019', 'Esmeriladora', 'Electrico', '8', '120')")
	c.execute("INSERT INTO inventario VALUES ('020', 'Flexómetro', 'Medición', '45', '4')")
	
	conn.commit()
	c.close()
	conn.close()
def agregar_producto(codigo, producto, laboratorio, cantidad, precio_und):
    """
    Agrega un nuevo producto a la tabla 'inventario' en la base de datos.

    Args:
        codigo (str): Código único del producto.
        producto (str): Nombre del producto.
        laboratorio (str): Categoría o sección del producto.
        cantidad (str): Cantidad en stock.
        precio_und (str): Precio por unidad.

    """
    try:
        conn = sqlite3.connect('base_inventario.db')  # Conectar a la base de datos
        c = conn.cursor()
        # Insertar el nuevo producto en la tabla
        c.execute(
            "INSERT INTO inventario (codigo, producto, laboratorio, cantidad, precio_und) VALUES (?, ?, ?, ?, ?)",
            (codigo, producto, laboratorio, cantidad, precio_und)
        )
        conn.commit()  # Confirmar cambios
        print(f"Producto '{producto}' agregado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al agregar el producto: {e}")
    finally:
        c.close()
        conn.close()


def consultar_todos_los_productos():
    """
    Consulta todos los productos en la tabla 'inventario' y los imprime.

    Returns:
        list: Lista de todos los productos en la tabla 'inventario'.
    """
    try:
        conn = sqlite3.connect('base_inventario.db')  # Conectar a la base de datos
        c = conn.cursor()
        # Consultar todos los productos
        c.execute("SELECT * FROM inventario")
        productos = c.fetchall()
        if productos:
            print("Productos en la base de datos:")
            for producto in productos:
                print(producto)
        else:
            print("No hay productos en la base de datos.")
        return productos
    except sqlite3.Error as e:
        print(f"Error al consultar los productos: {e}")
        return []
    finally:
        c.close()
        conn.close()

def actualizar_producto(codigo, nuevo_producto=None, nuevo_laboratorio=None, nueva_cantidad=None, nuevo_precio_und=None):
    """
    Actualiza los datos de un producto en la tabla 'inventario'.

    Args:
        codigo (str): Código único del producto a actualizar.
        nuevo_producto (str): Nuevo nombre del producto (opcional).
        nuevo_laboratorio (str): Nuevo laboratorio o categoría del producto (opcional).
        nueva_cantidad (str): Nueva cantidad en stock (opcional).
        nuevo_precio_und (str): Nuevo precio por unidad (opcional).

    Returns:
        bool: True si la actualización fue exitosa, False en caso contrario.
    """
    try:
        conn = sqlite3.connect('base_inventario.db')  # Conectar a la base de datos
        c = conn.cursor()

        # Generar la consulta dinámica según los valores proporcionados
        actualizaciones = []
        valores = []
        if nuevo_producto:
            actualizaciones.append("producto = ?")
            valores.append(nuevo_producto)
        if nuevo_laboratorio:
            actualizaciones.append("laboratorio = ?")
            valores.append(nuevo_laboratorio)
        if nueva_cantidad:
            actualizaciones.append("cantidad = ?")
            valores.append(nueva_cantidad)
        if nuevo_precio_und:
            actualizaciones.append("precio_und = ?")
            valores.append(nuevo_precio_und)

        if not actualizaciones:
            print("No se proporcionaron datos para actualizar.")
            return False

        valores.append(codigo)
        consulta = f"UPDATE inventario SET {', '.join(actualizaciones)} WHERE codigo = ?"
        c.execute(consulta, valores)
        conn.commit()

        if c.rowcount > 0:
            print(f"Producto con código '{codigo}' actualizado correctamente.")
            return True
        else:
            print(f"No se encontró un producto con el código '{codigo}'.")
            return False
    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")
        return False
    finally:
        c.close()
        conn.close()

def eliminar_producto(codigo):
    """
    Elimina un producto de la tabla 'inventario' en la base de datos.

    Args:
        codigo (str): Código único del producto a eliminar.

    Returns:
        bool: True si el producto fue eliminado, False si no se encontró.
    """
    try:
        conn = sqlite3.connect('base_inventario.db')  # Conectar a la base de datos
        c = conn.cursor()
        # Ejecutar la consulta para eliminar el producto
        c.execute("DELETE FROM inventario WHERE codigo = ?", (codigo,))
        conn.commit()

        if c.rowcount > 0:
            print(f"Producto con código '{codigo}' eliminado correctamente.")
            return True
        else:
            print(f"No se encontró un producto con el código '{codigo}'.")
            return False
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
        return False
    finally:
        c.close()
        conn.close()

# # Ejemplo de uso
# eliminar_producto('019')

# # Ejemplo de uso
# productos = consultar_todos_los_productos()

import sqlite3
import pandas as pd
import os
import platform

def generar_reporte_excel():
    """
    Genera un reporte en formato Excel con los productos de la base de datos.
    """
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('base_inventario.db')
        # Leer todos los productos de la tabla 'inventario'
        query = "SELECT * FROM inventario"
        df = pd.read_sql(query, conn)
        # Cerrar la conexión a la base de datos
        conn.close()
        
        # Guardar el DataFrame en un archivo Excel
        nombre_archivo = "reporte_inventario.xlsx"
        df.to_excel(nombre_archivo, index=False, engine='openpyxl')
        print(f"Reporte generado exitosamente: {nombre_archivo}")
        
        # Abrir el archivo Excel después de crearlo
        if platform.system() == 'Windows':
            os.startfile(nombre_archivo)  # Para Windows
        elif platform.system() == 'Darwin':  # macOS
            os.system(f"open {nombre_archivo}")
        else:  # Para Linux
            os.system(f"xdg-open {nombre_archivo}")
        
    except Exception as e:
        print(f"Error al generar el reporte: {e}")


