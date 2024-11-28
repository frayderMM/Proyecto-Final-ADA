from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import sys
from PyQt6.QtGui import QIcon, QFont,QPixmap
from PyQt6.QtCore import QSize, Qt, QDate,QTimer
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QPropertyAnimation, pyqtProperty
from PyQt6.QtWidgets import QGraphicsOpacityEffect


from Inventario_venta_PyQt import mainx
from gestionProducto import mainGestion

class PRINCIPAL(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        
        # Configuración de la ventana principal
        self.setWindowTitle("Gestión Invertario ")
        self.setGeometry(100, 100, 800, 600)

        
        # Crear un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        self.img_dir = os.path.join(os.path.dirname(__file__), "Images")
        # Añadir imagen de fondo
        central_widget.setStyleSheet(" background-repeat: no-repeat; background-position: center;")

        # Crear una etiqueta para el título
        title_label = QLabel("JB SOLCUIONES", self)
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: white;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Crear un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        central_widget.setLayout(layout)
        
        
        # Crear una imagen que no afecte la posición del botón
        image_label = QLabel(self)
        image_label.setPixmap(QPixmap(os.path.join(self.img_dir, 'centro.jpg')))
        image_label.setScaledContents(True)  
        image_label.setGeometry(0,170,1600,410)
        
        # Crear una etiqueta para mostrar texto
        self.text_label_tt = QLabel("Herramienta de control de productos ", self)
        self.text_label_tt.setGeometry(480, 480, 650, 250)
        # Cambiar el estilo y tamaño de la fuente
        self.text_label_tt.setStyleSheet("font-size: 25px; font-family: Arial; color: black; font-weight: bold;")

        
        
        # Crear una etiqueta para mostrar texto
        text_label_mesage = QLabel("En Ferretería JB soluciones, contamos con años de experiencia ofreciendo herramientas y materiales de construcción de la más alta calidad. \n                 Disponemos de un amplio catálogo de productos para todas tus necesidades, garantizando confianza, durabilidad y precios competitivos.", self)
        text_label_mesage.setGeometry(330, 490, 800, 300)
        # Cambiar el estilo y tamaño de la fuente
        text_label_mesage.setStyleSheet("font-size: 10px; font-family: Arial; color: black; font-weight: bold;")


        # Crear una etiqueta para mostrar texto
        self.text_label_titulo2 = QLabel("Gestor de operaciones", self)  # Añade esta línea antes de la línea 78
        self.text_label_titulo2.setGeometry(310, -20, 460, 100)
        self.text_label_titulo2.setStyleSheet("font-size: 40px; font-family: Arial; color: black; font-weight: bold;")

        
        
        # Crear una etiqueta para mostrar texto
        self.text_label_titulo = QLabel("JB SOLUCIONES", self)  # Añade esta línea antes de la línea 78
        self.text_label_titulo.setGeometry(400, 140, 400, 200)
        self.text_label_titulo.setStyleSheet("font-size: 40px; font-family: Arial; color: white; font-weight: bold;")

        # LOGOOOO
        image_label_logo = QLabel(self)
        image_label_logo.setPixmap(QPixmap(os.path.join(self.img_dir, 'logoJbSoluciones.jpeg')))
        image_label_logo.setScaledContents(True)  
        image_label_logo.setGeometry(0,0,220,170)
        
        # Crear una etiqueta para mostrar texto
        self.text_label_titulo.setGeometry(180, 140, 400, 200)
        # Cambiar el estilo y tamaño de la fuente
        self.text_label_titulo.setStyleSheet("font-size: 40px; font-family: Arial; color: white; font-weight: bold;")
        
        
        # Crear una etiqueta para mostrar texto
        self.text_label_reseña = QLabel("Estamos aquí para ofrecerte calidad y servicio\n en cada herramienta y material que necesites.", self)

        self.text_label_reseña.setGeometry(155, 220, 500, 300)
        # Cambiar el estilo y tamaño de la fuente
        self.text_label_reseña.setStyleSheet("font-size: 20px; font-family: Arial; color: white; ")
        
        
        
        # Crear una imagen que no afecte la posición del botón
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(os.path.join(self.img_dir, 'fotos.png')))
        self.image_label.setScaledContents(True)  
        self.image_label.setGeometry(880,170,400,410)
        
        # Crear una imagen que no afecte la posición del botón
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(os.path.join(self.img_dir, 'cintaJb.png')))
        self.image_label.setScaledContents(True)  
        self.image_label.setGeometry(880,20,430,150)
        
        
        
        
        #AGREGAR NOSOTROS 
        self.nosotros_button = QPushButton("  . \n  .", central_widget)
        self.nosotros_button.setFixedSize(200, 80)
        self.nosotros_button.setStyleSheet(" color: black; padding: 10px; border-radius: 0px; font-size: 20px; font-weight: bold")
        
        # Establecer el icono
        icon_path = os.path.join(self.img_dir, '..png')
        self.nosotros_button.setIcon(QIcon(icon_path))

        # Ajustar el tamaño del icono si es necesario
        self.nosotros_button.setIconSize(QSize(30, 30)) 
        self.nosotros_button.setGeometry(240,70,450,400)
        self.nosotros_button.setStyleSheet(" color: black; padding: 10px; border-radius: 0px; font-size: 20px; font-weight: bold")
        
        
        #AGREGAR GETIONAR
        self.gestionar_button = QPushButton("  GESTIONAR \n  PRODUCTO", central_widget)
        self.gestionar_button.setFixedSize(200, 80)
        self.gestionar_button.setStyleSheet(" color: black; padding: 10px; border-radius: 0px; font-size: 20px; font-weight: bold")

        # Establecer el icono
        icon_path = os.path.join(self.img_dir, 'gestion.png')
        self.gestionar_button.setIcon(QIcon(icon_path))

        # Ajustar el tamaño del icono si es necesario
        self.gestionar_button.setIconSize(QSize(30, 30)) 
        self.gestionar_button.setGeometry(450,70,450,400)
        self.gestionar_button.clicked.connect(self.mostrar_gestion)
        self.gestionar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.nosotros_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        # Crear una imagen que no afecte la posición del botón
        self.img_bd = QLabel(self)
        self.img_bd.setPixmap(QPixmap(os.path.join(self.img_dir, 'bd.png')))
        self.img_bd.hide()
        self.img_bd.setScaledContents(True)  
        self.img_bd.setGeometry(880,170,450,400)
        
        
        
        
        
        
        
        
        #AGREGAR PROCESO
        self.proceso_button = QPushButton("  EMITIR \n  FACTURA", central_widget)
        self.proceso_button.setFixedSize(180, 80)
        self.proceso_button.setStyleSheet(" color: black; padding: 10px; border-radius: 0px; font-size: 20px; font-weight: bold")
        
        # Establecer el icono
        icon_path = os.path.join(self.img_dir, 'reserva.png')
        self.proceso_button.setIcon(QIcon(icon_path))

        # Ajustar el tamaño del icono si es necesario
        self.proceso_button.setIconSize(QSize(30, 30)) 
        self.proceso_button.setGeometry(660,70,450,400)
        self.proceso_button.clicked.connect(self.mostrar_proceso)        
        self.proceso_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        
        
        
        # Crear una etiqueta para mostrar texto
        r1 = QLabel("Encuentra el auto perfecto para tu viaje\n     con comodidad y seguridad.", self)
        r1.setGeometry(440, 110, 3, 60)
        # Cambiar el estilo y tamaño de la fuente
        r1.setStyleSheet("background-color:black;font-size: 20px; font-family: Arial; color: black; ")

        # Crear una etiqueta para mostrar texto
        r2 = QLabel("Viaja sin preocupaciones, reserva tu auto\n     y disfruta del camino.", self)
        r2.setGeometry(650, 110, 3, 60)
        # Cambiar el estilo y tamaño de la fuente
        r2.setStyleSheet("background-color:black;font-size: 20px; font-family: Arial; color: black; ")
        
    
    def ocultar_gestion(self):
        self.fade_out_text(self.text_label_titulo, 2000, 1000)
        self.fade_out_text(self.text_label_reseña, 2000, 1000)
        
    def mostrar_gestion(self):
        mainGestion()
        
    def mostrar_proceso(self):
        mainx()
    def mostrar_nostros(self):
        self.text_label_titulo.hide()
        
        
    def fade_out_text(self, label, delay, duration):
        """Función para aplicar el desvanecimiento suave a una etiqueta de texto."""
        # Aplicar efecto de opacidad
        opacity_effect = QGraphicsOpacityEffect()
        label.setGraphicsEffect(opacity_effect)
        
        # Crear la animación para la opacidad
        animation = QPropertyAnimation(opacity_effect, b"opacity")
        animation.setDuration(duration)  # Duración de la animación
        animation.setStartValue(1)       # Opacidad inicial
        animation.setEndValue(0)         # Opacidad final (invisible)
        
        # Guardar la animación como atributo para que no sea eliminada por el recolector de basura
        if not hasattr(self, 'animations'):
            self.animations = []  # Crear una lista para almacenar las animaciones
        self.animations.append(animation)  # Agregar la animación a la lista
        
        # Iniciar la animación después de un retraso
        QTimer.singleShot(delay, animation.start)
        
        
    def fade_in_text(self, label, duration):
        """Función para volver a mostrar el texto (fade-in)."""
        opacity_effect = QGraphicsOpacityEffect()
        label.setGraphicsEffect(opacity_effect)

        fade_in = QPropertyAnimation(opacity_effect, b"opacity")
        fade_in.setDuration(duration)
        fade_in.setStartValue(0)
        fade_in.setEndValue(1)

        # Guardar la animación para evitar el garbage collector
        self.animations.append(fade_in)
        
        fade_in.start() 
def mainb():
    app = QApplication(sys.argv)
    main_window = PRINCIPAL()
    main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec())
def ja():
    print("holaaaaa mundooooo")
if __name__ == "__main__":
    mainb()