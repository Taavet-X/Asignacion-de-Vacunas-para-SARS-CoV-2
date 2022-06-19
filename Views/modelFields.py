from tkinter import *
import math
#from tkinter import ttk

class ModelFields(Frame):

	def __init__(self, parent, restricciones):
		super().__init__(parent)
		self.kits_bioseguridad = self.createEntry("Kits de Bioseguridad")
		self.unidades_vacunacion = self.createEntry("Unidades de Vacunacion")
		self.presupuesto_instalaciones = self.createEntry("Presupuesto Instalaciones")
		self.cualificacion = self.createEntry("Cualificacion")
		self.dosis_minima = self.createEntry("Dosis Minima")
		Limpiar = Button(self, text="Limpiar", command = self.limpiar)
		Limpiar.grid(column=1, row = int(len(self.winfo_children())/2)+1, columnspan=1,  sticky=(E, W))
		self.setValues(restricciones)

	def createEntry(self, name):
		label = Label(self, text = name, padx = 10, pady = 10, anchor="w")
		row = int(len(self.winfo_children())/2)
		label.grid(column=0, row = row, columnspan=1, sticky=(E, W))
		textVariable = StringVar()
		entry = Entry(self, textvariable = textVariable, borderwidth=1, relief="ridge", bg="white")
		entry.grid(column=1, row = row, columnspan=1,  sticky=(E, W))
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		return textVariable

	def limpiar(self):
		self.kits_bioseguridad.set("")
		self.unidades_vacunacion.set("")
		self.presupuesto_instalaciones.set("")
		self.cualificacion.set("")
		self.dosis_minima.set("")

	def setValues(self, restricciones):
		self.kits_bioseguridad.set(restricciones["kits_vacunacion"])
		self.unidades_vacunacion.set(restricciones["unidades_vacunacion"])
		self.presupuesto_instalaciones.set(restricciones["presupuesto_instalaciones"])
		self.cualificacion.set(restricciones["cualificacion"])
		self.dosis_minima.set(restricciones["dosis_minima"])



'''
root = Tk()

restricciones=ttk.Frame(root, padding=(3,3,12,12))
kitslbl = ttk.Label(restricciones, text="Kits")
kits = ttk.Entry(restricciones)
unidadesVacunacionlbl = ttk.Label(restricciones, text="Unidades Vacunacion")
unidadesVacunacion = ttk.Entry(restricciones)
presupuestoInstalbl = ttk.Label(restricciones, text="Presupuesto Instalaciones")
presupuestoInsta = ttk.Entry(restricciones)
cualificacionlbl = ttk.Label(restricciones, text="Cualificacion")
cualificacion = ttk.Entry(restricciones)
docsisMinlbl = ttk.Label(restricciones, text="Dosis Minima")
docsisMin = ttk.Entry(restricciones)

Limpiar = ttk.Button(restricciones, text="Limpiar")
Calcular = ttk.Button(restricciones, text="Calcular")

restricciones.grid(column=3, row=0,sticky=(N, S, E, W))
kitslbl.grid(column=0, row=0, columnspan=1, sticky=(N, W), padx=5)
kits.grid(column=1, row=0, columnspan=1, sticky=(N,E,W), pady=5, padx=5)
unidadesVacunacionlbl.grid(column=0, row=1, columnspan=1, sticky=(N,E, W), padx=5)
unidadesVacunacion.grid(column=1, row=1, columnspan=1, sticky=(N,E,W), pady=5, padx=5)
presupuestoInstalbl.grid(column=0, row=2, columnspan=1, sticky=(N, W), padx=5)
presupuestoInsta.grid(column=1, row=2, columnspan=1, sticky=(N,E,W), pady=5, padx=5)
cualificacionlbl.grid(column=0, row=3, columnspan=1, sticky=(N, W), padx=5)
cualificacion.grid(column=1, row=3, columnspan=1, sticky=(N,E,W), pady=5, padx=5)
docsisMinlbl.grid(column=0, row=4, columnspan=1, sticky=(N, W), padx=5)
docsisMin.grid(column=1, row=4, columnspan=1, sticky=(N,E,W), pady=10, padx=5)
Limpiar.grid(column=0, row=5,columnspan=4, sticky=(N,E,W), padx=10)
Calcular.grid(column=0, row=6,columnspan=4, sticky=(N,E,W), pady=10, padx=10)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

restricciones.columnconfigure(0, weight=3)
restricciones.columnconfigure(1, weight=3)
restricciones.columnconfigure(2, weight=3)
restricciones.columnconfigure(3, weight=1)
restricciones.columnconfigure(4, weight=1)
restricciones.rowconfigure(1, weight=1)

root.mainloop()
'''