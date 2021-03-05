# Cargar información desde un archivo de texto
# Retorna una lista de objetos de tipo Region resultado de la información cargada
KITS = "kits_vacunacion"
VACUNACION = "unidades_vacunacion"
PRESUPUESTO = "presupuesto_instalaciones"
CUALIFICACION = "cualificacion"
DOSIS = "dosis_minima"

from region import Region


def load_info(ruta: str):
    pass


# Cargar informacion de restricciones
def load_restric(ruta: str):
    pass


# Calcula el beneficio y dar la variable
def beneficio(regiones: list):
    # def myFunc(e):
    #   return len(e)

    # cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

    # cars.sort(key=myFunc)
    pass


# CRISTHIAN GARCIA
# Generar modelo: Recibe un diccionario con la información y ajusta el modelo
# con los datos.
# ... Hay 2 formas de hacerlo. Hacer el modelo en python añadiendo
# ... strings
def generate_model(regiones: list, restricciones: dict):
    n = len(regiones)
    variables = ""
    kits_seguridad = "\nconstraint "
    vacunacion = "\nconstraint ("
    costo_instalacion = "\nconstraint ("
    cualificacion = "\nconstraint "
    no_negatividad = ""
    z = "\nconstraint Z = "
    output = "\noutput [\"Z = \", show(Z), "
    # Definir las variables del problema
    for region in regiones:
        variables += "var int: " + region.variable + ";\n"

        if region.variable == "x" + str(n):
            kits_seguridad += str(region.kits_seguridad) + "*" + region.variable
            vacunacion += str(region.unidades_vacunacion) + "*" + region.variable
            costo_instalacion += str(region.costo_adecuacion) + "*" + region.variable
            cualificacion += str(region.cualificacion) + "*" + region.variable
            z += str(region.beneficio) + "*" + region.variable + ";\n\n"
            output += "\"\\n" + region.variable + " = \", show(" + region.variable + ")"
        else:
            kits_seguridad += str(region.kits_seguridad) + "*" + region.variable + " + "
            vacunacion += str(region.unidades_vacunacion) + "*" + region.variable + " + "
            costo_instalacion += str(region.costo_adecuacion) + "*" + region.variable + " + "
            cualificacion += str(region.cualificacion) + "*" + region.variable + " + "
            z += str(region.beneficio) + "*" + region.variable + " + "
            output += "\"\\n" + region.variable + " = \", show(" + region.variable + "),"
        no_negatividad += "constraint " + region.variable + " >= " + str(restricciones[DOSIS]) + ";\n"

    kits_seguridad += " <= " + str(restricciones[KITS]) + ";\n"
    vacunacion += ")/10000 <= " + str(restricciones[VACUNACION]) + ";\n"
    costo_instalacion += ")/500000 <= " + str(restricciones[PRESUPUESTO]) + ";\n"
    cualificacion += " >= " + str(restricciones[CUALIFICACION]) + ";\n\n"
    solve = "solve maximize Z;\n"

    output += "];"

    return variables + kits_seguridad + vacunacion + costo_instalacion + cualificacion + no_negatividad + z + solve + output


# Dado el modelo cargado en la función generate_model() resuelve el problema
def solve_model(model):
    pass


def main():
    region1 = Region("Este", 22, 2, 2, 90, 250, 0, 1)

    region2 = Region("Norte", 50, 2, 2, 80, 550, 0, 1)
    region3 = Region("Centro-Norte", 40, 2, 3, 110, 1000, 0, 1)
    region4 = Region("Oeste", 35, 3, 4, 95, 300, 2, 1)
    region5 = Region("Sur", 25, 3, 1, 100, 350, 4, 2)
    region6 = Region("Centro", 90, 4, 1, 70, 2600, 0, 1)
    region7 = Region("Noreste", 30, 5, 3, 120, 300, 3, 2)

    region1.variable = "x1"
    region2.variable = "x2"
    region3.variable = "x3"
    region4.variable = "x4"
    region5.variable = "x5"
    region6.variable = "x6"
    region7.variable = "x7"
    regiones = [region1, region2, region3, region4, region5, region6, region7]

    print(generate_model(regiones, {KITS: 2500000,
                                    VACUNACION: 300,
                                    PRESUPUESTO: 3500,
                                    CUALIFICACION: 1000,
                                    DOSIS: 10000
                                    }))
    # load_info("ruta")
    # load_restric("ruta")
    # beneficio()
    # generate_model()
    pass
