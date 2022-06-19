from tkinter import * 
from region import Region

class CreateRegion(Toplevel):

	def __init__(self, parent):
		super().__init__(parent)
		self.region = None
		self.transient(parent)
		#root = Tk()
		self.container = Frame(self, padx = 10, pady = 10);
		self.container.grid(column = 0, row = 0, sticky = (N, E, W, S))
		self.title("Crear Region")
		self.nombre = self.createEntry("Nombre")
		self.poblacion = self.createEntry("Poblacion")
		self.congeladores = self.createEntry("Congeladores")
		self.unidadesVacunacion = self.createEntry("Unidades de Vacunacion")
		self.costoAdecuacion = self.createEntry("Costo de Adecuacion")
		self.muertes = self.createEntry("Muertes")
		self.cualificacion = self.createEntry("Cualificacion")
		self.kitsBioseguridad = self.createEntry("Kits de Bioseguridad")
		btnCrear = Button(self.container)
		btnCrear["text"] = "Crear Region"
		btnCrear["command"] = self.createRegion
		btnCrear.grid(column = 0, row = len(self.container.winfo_children()), columnspan = 2, sticky = (W, E, S))
		self.container.rowconfigure(len(self.container.winfo_children()), weight = 1)
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		self.minsize(400, 400)

	def createEntry(self, name):
		label = Label(self.container, text = name, padx = 10, pady = 10, anchor="w")
		row = int(len(self.container.winfo_children())/2)
		label.grid(column=0, row = row, columnspan=1, sticky=(E, W))
		textVariable = StringVar()
		entry = Entry(self.container, textvariable = textVariable, borderwidth=1, relief="ridge", bg="white")
		entry.grid(column=1, row = row, columnspan=1,  sticky=(E, W))
		self.container.columnconfigure(0, weight=1)
		self.container.columnconfigure(1, weight=1)
		return textVariable

	def createRegion(self):
		self.region = Region(
			self.nombre.get(),
			self.poblacion.get(),
			self.congeladores.get(),
			self.unidadesVacunacion.get(),
			self.costoAdecuacion.get(),
			self.muertes.get(),
			self.cualificacion.get(),
			self.kitsBioseguridad.get()
			)
		self.destroy()

	def getRegion(self):
		return self.region

#CreateRegion()