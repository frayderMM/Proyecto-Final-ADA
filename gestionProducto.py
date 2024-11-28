import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QLabel, QLineEdit, QPushButton, QTableWidget
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont,QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Crear_base_datos import generar_reporte_excel

class ProductoManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("background-color: #f5f5f5;")

        # Crear un QLabel para la imagen de fondo
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'images', 'fondo-metalico.png')))  # Asegúrate de que la imagen exista
        self.background_label.setScaledContents(True)  # Asegura que la imagen se redimensione con la ventana
        self.background_label.setGeometry(0, 0, 1400, 800)  # Ajustar al tamaño de la ventana
        

        # Fuentes y colores
        label_font = QFont("Arial", 12, QFont.Bold)
        input_font = QFont("Arial", 12)
        button_font = QFont("Arial", 12, QFont.Bold)

        # Crear Widgets
        self.label_codigo = QLabel("Código:", self)
        self.label_codigo.setFont(label_font)
        self.label_codigo.move(20, 20)
        self.input_codigo = QLineEdit(self)
        self.input_codigo.setFont(input_font)
        self.input_codigo.setGeometry(150, 20, 620, 30)

        self.label_producto = QLabel("Producto:", self)
        self.label_producto.setFont(label_font)
        self.label_producto.move(20, 70)
        self.input_producto = QLineEdit(self)
        self.input_producto.setFont(input_font)
        self.input_producto.setGeometry(150, 70, 620, 30)

        self.label_laboratorio = QLabel("Categoria:", self)
        self.label_laboratorio.setFont(label_font)
        self.label_laboratorio.move(20, 120)
        self.input_laboratorio = QLineEdit(self)
        self.input_laboratorio.setFont(input_font)
        self.input_laboratorio.setGeometry(150, 120, 620, 30)

        self.label_cantidad = QLabel("Cantidad:", self)
        self.label_cantidad.setFont(label_font)
        self.label_cantidad.move(20, 170)
        self.input_cantidad = QLineEdit(self)
        self.input_cantidad.setFont(input_font)
        self.input_cantidad.setGeometry(150, 170, 620, 30)

        self.label_precio = QLabel("Precio:", self)
        self.label_precio.setFont(label_font)
        self.label_precio.move(20, 220)
        self.input_precio = QLineEdit(self)
        self.input_precio.setFont(input_font)
        self.input_precio.setGeometry(150, 220, 620, 30)

        # Botones
        self.btn_agregar = QPushButton("  Agregar", self)
        self.btn_agregar.setFont(button_font)
        self.btn_agregar.setGeometry(820, 20, 150, 40)
        self.btn_agregar.setStyleSheet("background-color: #4caf50; color: white;")
        self.btn_agregar.clicked.connect(self.agregar_producto)
        # Establecer el icono
        self.img_dir = os.path.join(os.path.dirname(__file__), 'images')
        icon_path = os.path.join(self.img_dir, 'add.png')
        self.btn_agregar.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_agregar.setIconSize(QSize(30, 30))

        self.btn_actualizar = QPushButton("  Actualizar", self)
        self.btn_actualizar.setFont(button_font)
        self.btn_actualizar.setGeometry(820, 80, 150, 40)
        self.btn_actualizar.setStyleSheet("background-color: #2196f3; color: white;")
        self.btn_actualizar.clicked.connect(self.actualizar_producto)
        icon_path = os.path.join(self.img_dir, 'update.png')
        self.btn_actualizar.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_actualizar.setIconSize(QSize(30, 30))

        self.btn_eliminar = QPushButton("  Eliminar", self)
        self.btn_eliminar.setFont(button_font)
        self.btn_eliminar.setGeometry(820, 140, 150, 40)
        self.btn_eliminar.setStyleSheet("background-color: #f44336; color: white;")
        self.btn_eliminar.clicked.connect(self.eliminar_producto)
        icon_path = os.path.join(self.img_dir, 'eliminar.png')
        self.btn_eliminar.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_eliminar.setIconSize(QSize(30, 30))


         # Crear una imagen que no afecte la posición del botón
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(os.path.join(self.img_dir, 'herramientas.jpg')))
        self.image_label.setScaledContents(True)  
        self.image_label.setGeometry(1000,260,350,400)
        

        self.btn_consultar = QPushButton("  Limpiar", self)
        self.btn_consultar.setFont(button_font)
        self.btn_consultar.setGeometry(820, 200, 150, 40)
        self.btn_consultar.setStyleSheet("background-color: #ff9800; color: white;")
        self.btn_consultar.clicked.connect(self.limpiar)
        icon_path = os.path.join(self.img_dir, 'clear.png')
        self.btn_consultar.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_consultar.setIconSize(QSize(30, 30))
        

        self.btn_reporte = QPushButton("  Reporte Excel", self)
        self.btn_reporte.setFont(button_font)
        self.btn_reporte.setGeometry(550, 665, 200, 30)
        self.btn_reporte.setStyleSheet("background-color: #8eacf9 ; color: white;")
        self.btn_reporte.clicked.connect(generar_reporte_excel)
        icon_path = os.path.join(self.img_dir, 'informe.png')
        self.btn_reporte.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_reporte.setIconSize(QSize(30, 30))


        self.btn_salir = QPushButton("  Salir", self)
        self.btn_salir.setFont(button_font)
        self.btn_salir.setGeometry(750, 665, 200, 30)
        self.btn_salir.setStyleSheet("background-color: #8eacf9 ; color: white;")
        self.btn_salir.clicked.connect(self.close)
        icon_path = os.path.join(self.img_dir, 'close.png')
        self.btn_salir.setIcon(QIcon(icon_path))
        # Ajustar el tamaño del icono si es necesario
        self.btn_salir.setIconSize(QSize(30, 30))

        # Tabla para mostrar productos
        self.table_productos = QTableWidget(self)
        self.table_productos.setColumnCount(5)
        self.table_productos.setHorizontalHeaderLabels(
            ["Código", "Producto", "Categoria", "Cantidad", "Precio"])
        self.table_productos.setGeometry(20, 280, 950, 380)
        self.table_productos.horizontalHeader().setStretchLastSection(True)
        self.table_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table_productos.setStyleSheet("background-color: white; border: 1px solid gray;")
        self.table_productos.setFont(QFont("Arial", 10))
        self.table_productos.horizontalHeader().setStyleSheet("background-color: #e0e0e0; font-weight: bold;")
        self.table_productos.setAlternatingRowColors(True)
        self.table_productos.setStyleSheet("""
            QTableWidget {
                background-color: white;
                alternate-background-color: #f9f9f9;
            }
            QHeaderView::section {
                background-color: #d6d6d6;
                font-weight: bold;
            }
        """)
        # Agregar una fila para los filtros
        self.add_filter_row()

        # Conectar la señal de selección de la tabla
        self.table_productos.cellClicked.connect(self.llenar_campos)

        # Inicializar la base de datos
        self.init_db()
        self.consultar_productos()
    
    def add_filter_row(self):
        self.table_productos.setRowCount(1)  # Primera fila para filtros
        self.filter_inputs = []  # Almacenar los filtros

        for col in range(self.table_productos.columnCount()):
            filter_input = QLineEdit(self)
            filter_input.setPlaceholderText(f"Filtrar {self.table_productos.horizontalHeaderItem(col).text()}")
            filter_input.textChanged.connect(self.filter_table)
            self.table_productos.setCellWidget(0, col, filter_input)
            self.filter_inputs.append(filter_input)

    def filter_table(self):
        filters = [filter_input.text().lower() for filter_input in self.filter_inputs]

        for row in range(1, self.table_productos.rowCount()):
            show_row = True
            for col, filter_text in enumerate(filters):
                item = self.table_productos.item(row, col)
                if filter_text and item and filter_text not in item.text().lower():
                    show_row = False
                    break
            self.table_productos.setRowHidden(row, not show_row)

    def consultar_productos(self):
        try:
            conn = sqlite3.connect('base_inventario.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventario")
            productos = cursor.fetchall()
            conn.close()

            self.table_productos.setRowCount(len(productos) + 1)  # +1 para la fila de filtros
            for row_idx, producto in enumerate(productos, start=1):  # Empieza en la segunda fila
                for col_idx, value in enumerate(producto):
                    self.table_productos.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    def limpiar(self):
        """Limpia todos los campos de entrada."""
        self.input_codigo.clear()
        self.input_producto.clear()
        self.input_laboratorio.clear()
        self.input_cantidad.clear()
        self.input_precio.clear()
    def llenar_campos(self, fila, columna):
        # Evita llenar los campos si se selecciona la fila de filtros
        if fila == 0:
            return
        self.input_codigo.setText(self.table_productos.item(fila, 0).text())
        self.input_producto.setText(self.table_productos.item(fila, 1).text())
        self.input_laboratorio.setText(self.table_productos.item(fila, 2).text())
        self.input_cantidad.setText(self.table_productos.item(fila, 3).text())
        self.input_precio.setText(self.table_productos.item(fila, 4).text())
    def init_db(self):
        conn = sqlite3.connect('base_inventario.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventario (
                codigo TEXT PRIMARY KEY,
                producto TEXT,
                laboratorio TEXT,
                cantidad TEXT,
                precio_und TEXT
            )
        """)
        conn.commit()
        conn.close()

    def actualizar_producto(self):
        codigo = self.input_codigo.text()
        producto = self.input_producto.text()
        laboratorio = self.input_laboratorio.text()
        cantidad = self.input_cantidad.text()
        precio = self.input_precio.text()

        if not codigo:
            QMessageBox.warning(self, "Error", "El código es obligatorio para actualizar.")
            return

        try:
            conn = sqlite3.connect('base_inventario.db')
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE inventario
                SET producto = ?, laboratorio = ?, cantidad = ?, precio_und = ?
                WHERE codigo = ?
            """, (producto, laboratorio, cantidad, precio, codigo))
            conn.commit()
            conn.close()
            if cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", "Producto actualizado correctamente.")
            else:
                QMessageBox.warning(self, "Error", "No se encontró el producto con ese código.")
            self.consultar_productos()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def eliminar_producto(self):
        codigo = self.input_codigo.text()
        if not codigo:
            QMessageBox.warning(self, "Error", "El código es obligatorio para eliminar.")
            return

        try:
            conn = sqlite3.connect('base_inventario.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inventario WHERE codigo = ?", (codigo,))
            conn.commit()
            conn.close()
            if cursor.rowcount > 0:
                QMessageBox.information(self, "Éxito", "Producto eliminado correctamente.")
            else:
                QMessageBox.warning(self, "Error", "No se encontró el producto con ese código.")
            self.consultar_productos()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    def agregar_producto(self):
        codigo = self.input_codigo.text()
        producto = self.input_producto.text()
        laboratorio = self.input_laboratorio.text()
        cantidad = self.input_cantidad.text()
        precio = self.input_precio.text()

        if not codigo or not producto or not laboratorio or not cantidad or not precio:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            conn = sqlite3.connect('base_inventario.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventario VALUES (?, ?, ?, ?, ?)",
                           (codigo, producto, laboratorio, cantidad, precio))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Éxito", "Producto agregado correctamente.")
            self.consultar_productos()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "El código ya existe.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))



def mainGestion():
    app = QApplication(sys.argv)
    window = ProductoManager()
    window.showMaximized()
    sys.exit(app.exec_())
if __name__ == "__main__":
    
    mainGestion()