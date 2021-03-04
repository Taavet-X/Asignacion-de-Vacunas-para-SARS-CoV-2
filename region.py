class Region:

    def __init__(self, nombre, poblacion, congeladores, unidades_vacunacion, costo_adecuacion, muertes, cualificacion):
        self.nombre = nombre
        self.poblacion = poblacion
        self.congeladores = congeladores
        self.unidades_vacunacion = unidades_vacunacion
        self.costo_adecuacion = costo_adecuacion
        self.muertes = muertes
        self.cualificacion = cualificacion
        self.beneficio = 0
        self.variable = ""
