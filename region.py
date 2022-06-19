class Region:

    #Region  Poblacion   Congeladores    UnidadesVacunacion  CostoAdecuacion Muertes Cualificacion KitsBioseguridad
    def __init__(self, nombre, poblacion, congeladores, unidades_vacunacion, costo_adecuacion, muertes, cualificacion,
                 kits_seguridad):
        self.nombre = nombre
        self.poblacion = int(poblacion)
        self.congeladores = int(congeladores)
        self.unidades_vacunacion = int(unidades_vacunacion)
        self.costo_adecuacion = int(costo_adecuacion)
        self.muertes = int(muertes)
        self.cualificacion = int(cualificacion)
        self.beneficio = 0
        self.variable = ""
        self.kits_seguridad = int(kits_seguridad)
