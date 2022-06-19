from tkinter import *
from Views.RegionForm import CreateRegion

class Table(Frame):

	def __init__(self, parent, listaRegiones):
		super().__init__(parent, borderwidth=1, relief="ridge")
		self.parent = parent
		self.listaRegiones = listaRegiones
		self.createHeaders()
		
		verticalScroll = Scrollbar(self)
		verticalScroll.grid(column = 1, row = 1, sticky=(N, S))
		self.rowContainer = Canvas(self)
		self.rowContainer.grid(column = 0, row = 1, sticky=(N, S, W, E))		
		self.rowContainer["yscrollcommand"] = verticalScroll.set	
		self.rowContainer.columnconfigure(0, weight = 1)
		self.rowContainer.configure(yscrollcommand=verticalScroll.set)	
		self.createRows()	
		self.columnconfigure(0, weight=1)
		#self.columnconfigure(1, weight=1)
		#self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)

		btnCrearRegion = Button(self)
		btnCrearRegion["text"] = "Crear Una Nueva Region"
		btnCrearRegion["command"] = self.crearRegion
		btnCrearRegion.grid(column = 0, row = 2, sticky = (E, W))
		self.rowconfigure(2, weight=1)

	def crearRegion(self):
		form = CreateRegion(self.parent)
		self.parent.wait_window(form)
		region = form.getRegion()
		if not (region == None):
			self.addRow(region)
			self.listaRegiones.append(region)

	def createHeaders(self):
		headers = Frame(self)
		headers.grid(column = 0, row = 0, columnspan = 1, sticky = (N, E, S, W))

		texts = ["Region", "Poblacion", "Congeladores", "Unidades Vacunacion", "Costo Adecuacion", "Muertes", "Cualificacion", "KitsBioseguridad", ""]
		for i in range(len(texts)):
			Label(headers, text = texts[i]).grid(column = i, row = 0, columnspan = 1, rowspan = 1, sticky = (N, E, S, W))
			headers.columnconfigure(i, weight = 1)
		headers.rowconfigure(0, weight = 1)

	def createRows(self):
		for region in self.listaRegiones:
			row(self, region)
			#self.rowContainer.rowconfigure(self.rowContainer.winfo_children(), weight = 1)

	def addRow(self, region):
		row(self, region)

	def deleteRow(self, row):
		print("Deleting a row ", row.nombre)		
		self.listaRegiones.remove(row.region)
		row.grid_forget()		


class row(Frame):

	def __init__(self, table, region):		
		self.region = region
		super().__init__(table.rowContainer)
		#self.row = row = Frame(table)
		self.grid(column=0, row=len(table.rowContainer.winfo_children())-1, sticky=(N, E, W))

		self.nombre = self.createEntry()
		self.poblacion = self.createEntry()
		self.congeladores = self.createEntry()
		self.unidades_vacunacion = self.createEntry()
		self.costo_adecuacion = self.createEntry()
		self.muertes = self.createEntry()
		self.cualificacion = self.createEntry()
		self.kits_seguridad = self.createEntry()
		self.loadValues()

		edit = Button(self, text="Editar", command = lambda: print("editar ", self.region.nombre))
		edit.grid(column=8, row=0, columnspan=1, sticky=(N, E, W, S))
		self.columnconfigure(8, weight=1)

		eliminar = Button(self, text="Eliminar", command = lambda: table.deleteRow(self))
		eliminar.grid(column=9, row=0, columnspan=1, sticky=(N, E, W, S))
		self.columnconfigure(9, weight=1)

	def createEntry(self):
		textVariable = StringVar()
		entry = Entry(self, textvariable = textVariable, borderwidth=1, relief="ridge", bg="white")
		entry.grid(column=len(self.winfo_children())-1, row=0, columnspan=1, sticky=(N, E, W, S))
		self.columnconfigure(len(self.winfo_children())-1, weight=1)
		return textVariable

	def loadValues(self):
		self.nombre.set(self.region.nombre)
		self.poblacion.set(self.region.poblacion)
		self.congeladores.set(self.region.congeladores)
		self.unidades_vacunacion.set(self.region.unidades_vacunacion)
		self.costo_adecuacion.set(self.region.costo_adecuacion)
		self.muertes.set(self.region.muertes)
		self.cualificacion.set(self.region.cualificacion)
		self.kits_seguridad.set(self.region.kits_seguridad)