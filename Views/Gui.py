from tkinter import *
from Views.Table import Table
from Views.modelFields import ModelFields
import model

class Gui:

	def __init__(self, listaRegiones, restricciones):
		self.listaRegiones = listaRegiones
		self.restricciones = restricciones
		self.createGui()

	def createGui(self):
		root = Tk()
		root.title("Proyecto Complejidad y Optimizacion")

		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Guardar", command= lambda : print("Guardar"))
		menubar.add_cascade(label="Archivo", menu=filemenu)

		content = Frame(root, padx=10, pady=10)
		content.grid(column=0, row=0, columnspan = 1, rowspan = 1, sticky=(N, S, E, W))
		self.createTable(content)
		self.createOutput(content)
		self.createInputs(content)
		self.createButtons(content)

		root.columnconfigure(0, weight=1)
		root.rowconfigure(0, weight=1)
		content.columnconfigure(0, weight=3)
		content.columnconfigure(1, weight=3)
		content.columnconfigure(2, weight=3)
		content.rowconfigure(1, weight=2)
		content.rowconfigure(3, weight=2)
		root.minsize(700, 500)

		root.config(menu=menubar)
		root.mainloop()

	def createTable(self, parent):
		table = Table(parent, self.listaRegiones)
		table.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))

	def createOutput(self, parent):
		container = Frame(parent)		
		container.grid(column=0, row=3, columnspan=2, rowspan=2, sticky=(N, S, E, W))
		verticalScroll = Scrollbar(container)
		verticalScroll.grid(column = 3, row = 0,sticky=(N, S))
		self.output = Text(container, height=10)
		self.output.grid(column=0, row=0, sticky=(N, S, E, W))
		self.output["yscrollcommand"] = verticalScroll.set
		container.columnconfigure(0, weight=1)
		container.rowconfigure(0, weight=1)
		

	def createInputs(self, parent):
		self.modelFields = ModelFields(parent, self.restricciones)
		self.modelFields.grid(column=2, row=0, columnspan = 1, sticky=(N, S, E, W))

	def createButtons(self, parent):
		run = Button(parent, text="Ejecutar Modelo")
		run.grid(column=2, row=3, columnspan = 1)
		run["command"] = self.ejecutarModelo

	def ejecutarModelo(self):
		print("Ejecutando Modelo")


		self.restricciones["kits_vacunacion"] = int(self.modelFields.kits_bioseguridad.get())
		self.restricciones["unidades_vacunacion"] = int(self.modelFields.unidades_vacunacion.get())
		self.restricciones["presupuesto_instalaciones"] = int(self.modelFields.presupuesto_instalaciones.get())
		self.restricciones["cualificacion"] = int(self.modelFields.cualificacion.get())
		self.restricciones["dosis_minima"] = int(self.modelFields.dosis_minima.get())

		'''
		self.output.insert(1.0,  self.modelFields.kits_bioseguridad.get() + "\n")
		self.output.insert(1.0, self.modelFields.unidades_vacunacion.get()+ "\n")
		self.output.insert(1.0, self.modelFields.presupuesto_instalaciones.get()+ "\n")
		self.output.insert(1.0, self.modelFields.cualificacion.get()+ "\n")
		self.output.insert(1.0, self.modelFields.dosis_minima.get()+ "\n")
		'''
		model.beneficio(self.listaRegiones)
		self.output.insert(1.0, model.init_solver2(self.listaRegiones, self.restricciones))
