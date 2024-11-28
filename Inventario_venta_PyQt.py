'''
	Autor : Marco Jhoel Churata Torres
	Fecha : 04 - 06 - 2020
	Nombre : Inventario_venta_PyQt.py
	Descripcion : Estuve haciendo este programa ... por algunos dias
					se los dejo aqui por si les sirve de algo.Gracias
'''
from datetime import datetime
import requests
import json
import re
import webbrowser

from Inventario_venta_UI import *
from datetime import date
import sqlite3


def eliminar_filas_venta():
	conn=sqlite3.connect('base_inventario.db')
	c=conn.cursor()
	c.execute('DELETE  FROM ventas ')
	conn.commit()

def base_datos(fila,columna):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM inventario')
	rows=cursor.fetchall()
	return rows[fila][columna]

def base_ventas(fila,columna):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM ventas')
	rows=cursor.fetchall()
	return rows[fila][columna]
	
def escribir_base_datos(producto,cantidad,unidades,precio_und,importe):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute("INSERT INTO ventas values (\'"+producto+"\',\'"+cantidad+"\',\'"+unidades+"\',\'"+precio_und+"\',\'"+importe+"')")
	con.commit()
	cursor.close()
	con.close()
	
def lista_ventas(vendedor,cliente,tipo_pago,fecha_venta,monto_total):
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute("INSERT INTO ventas_dia values (\'"+vendedor+"\',\'"+cliente+"\',\'"+tipo_pago+"\',\'"+fecha_venta+"\',\'"+monto_total+"')")
	con.commit()
	cursor.close()
	con.close()
	
def monto_total(catd_elem):
	monto_total_venta=0
	for valor in range(0,catd_elem):
		monto_total_venta=int(base_ventas(valor,4))+monto_total_venta
		#print(monto_total_venta)
	#print(monto_total_venta)
	return monto_total_venta
	
def elemtos_ventas():
	con=sqlite3.connect('base_inventario.db')
	cursor=con.cursor()
	cursor.execute('SELECT * FROM ventas')
	rows=cursor.fetchall()
	catd_elem=len(rows)
	return catd_elem
def eliminar_todos_los_datos_ventas():
    con = sqlite3.connect('base_inventario.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM ventas')  # Elimina todos los registros de la tabla ventas
    con.commit()
    con.close()
    print("Todos los datos de ventas han sido eliminados.")
eliminar_todos_los_datos_ventas()
from PyQt5 import QtWidgets, QtCore
import sqlite3
from datetime import date# Asegúrate de que tu archivo UI sea correcto

class MainWindow(QtWidgets.QMainWindow, Ui_VENTANA):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)  # Configura la interfaz desde el archivo UI

		# Inicialización
		self.fecha.setText(str(date.today()))
		self.vendedor.setText("Juan Perez")

		# Conexión a la base de datos
		conn = sqlite3.connect('base_inventario.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM inventario')  # Obtener todos los productos
		productos = cursor.fetchall()
		conn.close()

		# Ajustar la tabla según el número de productos
		self.tabla_int.setRowCount(len(productos))  # Establece el número de filas dinámicamente

		# Llenar la tabla con los datos de la base de datos
		for fila, producto in enumerate(productos):
			for columna, valor in enumerate(producto):
				item = self.tabla_int.item(fila, columna)
				if not item:
					item = QtWidgets.QTableWidgetItem()
					self.tabla_int.setItem(fila, columna, item)
				item.setText(str(valor))

		# Conectar señales
		self.tabla_int.cellClicked.connect(self.handle_row_click)
		self.total_general.textChanged.connect(self.actIGV)
		self.bot_agregar.clicked.connect(self.accion)
		self.generar_venta.clicked.connect(self.gen_vent)
		self.terminar.clicked.connect(self.terminar_venta)

		# Crear un botón de "Salir" manualmente
		self.salir_button = QtWidgets.QPushButton("Salir", self)
		self.salir_button.setGeometry(530, 630, 240, 40)  # Establece la posición y el tamaño
		self.salir_button.clicked.connect(self.salir)

	def salir(self):
		# Método para cerrar la aplicación
		self.close()

	def handle_row_click(self, row, column):
		"""
		Captura el clic en una fila de la tabla y actualiza el campo 'codigo' con el código del producto.
		:param row: Índice de la fila seleccionada.
		:param column: Índice de la columna seleccionada.
		"""
		# Obtener el código de la fila seleccionada (asumiendo que está en la columna 0)
		item = self.tabla_int.item(row, 0)  # Columna 0 para el código del producto
		if item:
			codigo = item.text()
			self.cod_bus.setText(codigo)  # Actualiza el campo de entrada con el código
			print(f"Código seleccionado: {codigo}")

	def actIGV(self):
		monto_general = self.total_general.text()
		self.lineEdit_14.setText(f"{float(monto_general) * 0.18:.2f}")
		valor_igv = self.lineEdit_14.text()

		print("MONTO GENERAL!!!!!",monto_general, valor_igv)
		

	def accion(self):
		#aea=self.cod_bus.text()
		for valor in range(0,10):
			if(base_datos(valor,0)==self.cod_bus.text()):
				self.nom_pro.setText(base_datos(valor,1))
				self.Lab.setText(base_datos(valor,2))
				self.p_unit.setText(base_datos(valor,4))
				cant=self.spinBox.text()
				monto_und=int(base_datos(valor,4))*int(cant)
				if(int(cant)>0):
					self.monto_t.setText(str(monto_und)+".00")
				else:
					self.monto_t.setText(".00")
	
	def gen_vent(self):
		_translate=QtCore.QCoreApplication.translate
		producto=self.nom_pro.text()
		cantidad=self.spinBox.text()
		unidades="und"
		precio_und=self.p_unit.text()
		importe=int(cantidad)*int(precio_und)
		escribir_base_datos(producto,cantidad,unidades,precio_und,str(importe))
		cnd_elem=elemtos_ventas()
		item=self.boleta.item(cnd_elem-1,0)
		item.setText(_translate("VENTANA",producto))
		item=self.boleta.item(cnd_elem-1,1)
		item.setText(_translate("VENTANA",cantidad))
		item=self.boleta.item(cnd_elem-1,2)
		item.setText(_translate("VENTANA",unidades))
		item=self.boleta.item(cnd_elem-1,3)
		item.setText(_translate("VENTANA",precio_und))
		item=self.boleta.item(cnd_elem-1,4)
		item.setText(_translate("VENTANA",str(importe)+'.00'))
		self.total_general.setText(str(monto_total(cnd_elem))+'.00')




		
	def terminar_venta(self):
		
		items = []
		productos = []
		for fila in range(self.tabla_int.rowCount()):
			codigo = self.tabla_int.item(fila, 0).text() if self.tabla_int.item(fila, 0) else ''
			nombre_producto = self.tabla_int.item(fila, 1).text() if self.tabla_int.item(fila, 1) else ''
			productos.append({'codigo': codigo, 'nombre_producto': nombre_producto})
		
		for fila in range(self.boleta.rowCount()):
			detalle = {}
			# Asumiendo que las columnas son: Producto, Cantidad, Unidad, P.Unit, Importe
			detalle["producto"] = self.boleta.item(fila, 0).text() if self.boleta.item(fila, 0) else ""
			detalle["cantidad"] = self.boleta.item(fila, 1).text() if self.boleta.item(fila, 1) else ""
			detalle["unidad"] = self.boleta.item(fila, 2).text() if self.boleta.item(fila, 2) else ""
			detalle["precio_unitario"] = self.boleta.item(fila, 3).text() if self.boleta.item(fila, 3) else ""
			detalle["importe"] = self.boleta.item(fila, 4).text() if self.boleta.item(fila, 4) else ""
			# for i in productos:
			code = ""
			for i in productos:
				if detalle["producto"] == i ["nombre_producto"]:
					code = i["codigo"]
			if detalle["producto"] != "-":
				producto = {
					"producto": detalle["producto"],
					"cantidad": detalle["cantidad"],
					"precio_base": detalle["precio_unitario"],
					"codigo_sunat": "-",
					"codigo_producto": code,
					"codigo_unidad": "NIU",
					"tipo_igv_codigo": "10"
				}
				items.append(producto)

		# Formatear el resultado con json.dumps para usar comillas dobles
		print("Detalles de la venta:", json.dumps(items, indent=4))
		

		razon_social_nombres= str(self.cliente.text())
		numero_documento= 10407086274#str(self.num_doc.text())
		
		codigo_tipo_entidad= "6"
		cliente_direccion= "Av. Morales Duarez 168"



		
		
		# URL de la API
		url = "https://facturaciondirecta.com/API_SUNAT/post.php"
		# Datos de la solicitud
		payload = {
			"empresa": {
				"ruc": "20604051984",
				"razon_social": "FACTURACION ELECTRONICA JB soluciones",
				"nombre_comercial": "FACTURACION INTEGRAL",
				"domicilio_fiscal": "AV. LA MOLINA NRO. 570",
				"ubigeo": "150114",
				"urbanizacion": "RESIDENCIAL MONTERRICO",
				"distrito": "LA MOLINA",
				"provincia": "LIMA",
				"departamento": "LIMA",
				"modo": "0",
				"usu_secundario_produccion_user": "MODDATOS",
				"usu_secundario_produccion_password": "MODDATOS"
			},
			"cliente": {
				"razon_social_nombres": razon_social_nombres,
				"numero_documento": numero_documento,
				"codigo_tipo_entidad":codigo_tipo_entidad,
				"cliente_direccion": cliente_direccion
			},
			"venta": {
				"serie": "FF03",
				"numero": "53953",
				"fecha_emision": datetime.now().strftime("%Y-%m-%d"),
				"hora_emision": datetime.now().time().strftime("%H:%M:%S"),
				"fecha_vencimiento": "",
				"moneda_id": "2",
				"forma_pago_id": "1",
				"total_gravada": self.total_general.text(),
				"total_igv": self.lineEdit_14.text(),
				"total_exonerada": "",
				"total_inafecta": "",
				"tipo_documento_codigo": "01",
				"nota": "notas o comentarios"
			},
			"items": items
		}

		# Encabezados HTTP
		headers = {
			"Content-Type": "application/json",
			"Accept": "application/json"
		}

		# Llamar a la función
		enviar_factura_api_sunat(url, payload, headers)


def enviar_factura_api_sunat(url, payload, headers):
		"""
		Envia una solicitud POST a la API de facturación y procesa la respuesta.

		Args:
			url (str): URL de la API.
			payload (dict): Datos a enviar a la API en formato JSON.
			headers (dict): Encabezados HTTP para la solicitud.

		Returns:
			dict: Respuesta JSON procesada de la API, si está disponible.
		"""
		try:
			response = requests.post(url, data=json.dumps(payload), headers=headers)

			# Inspeccionar la respuesta completa
			print("=== Respuesta Cruda de la API ===")
			

			# Extraer el contenido JSON de la respuesta usando una expresión regular
			match = re.search(r'({.*})', response.text, re.DOTALL)
			if match:
				raw_json = match.group(1)  # Captura solo el JSON
				try:
					data = json.loads(raw_json)  # Decodifica el JSON
					print("=== Respuesta de la API (Formato JSON) ===")
					print(json.dumps(data, indent=4, ensure_ascii=False))
					# Abrir el PDF en el navegador si existe
					pdf_url = data['data'].get('ruta_pdf')
					if pdf_url:
						print(f"Abriendo el PDF en el navegador: {pdf_url}")
						webbrowser.open(pdf_url)
					else:
						print("No se encontró el URL del PDF en la respuesta.")
					return data
				except json.JSONDecodeError as e:
					print(f"Error al procesar el JSON extraído: {e}")
			else:
				print("No se encontró un JSON válido en la respuesta.")
		except requests.exceptions.RequestException as e:
			print(f"Error al realizar la solicitud: {e}")	
def mainx():
	app=QtWidgets.QApplication([])
	window=MainWindow()
	window.showMaximized()

	app.exec_()	
if __name__=="__main__":
	#crear_tabla
	mainx()
