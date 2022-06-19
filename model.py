from minizinc import Solver, Model, Instance

from region import Region

KITS = "kits_vacunacion"
VACUNACION = "unidades_vacunacion"
PRESUPUESTO = "presupuesto_instalaciones"
CUALIFICACION = "cualificacion"
DOSIS = "dosis_minima"


# Cargar información desde un archivo de texto
# Retorna una lista de objetos de tipo Region resultado de la información cargada
def load_info(ruta: str):
    file = open(ruta, "r")
    regiones = []

    info = file.read().split("\n")
    file.close()

    for i in range(len(info)):
        line = info[i].split(",")
        if i > 0:
            region = Region(line[0],
                            int(line[1]),
                            int(line[2]),
                            int(line[3]),
                            int(line[4]),
                            int(line[5]),
                            int(line[6]),
                            int(line[7]))
            regiones.append(region)
    beneficio(regiones)
    return regiones


# Cargar informacion de restricciones
def load_restric(ruta: str):
    file = open(ruta, "r")
    restricciones = {}

    info = file.read().split("\n")
    file.close()

    for line in info:
        restrict = line.split(":")
        restricciones[restrict[0]] = restrict[1]

    return restricciones


# Calcula el beneficio y dar la variable
def beneficio(regiones: list):
    def muertes(e: Region):
        return e.muertes

    def congeladores(e: Region):
        return e.congeladores

    regiones.sort(key=muertes)
    regiones.sort(key=congeladores)
    i = 1

    for region in regiones:
        region.beneficio = i
        region.variable = f"x{i}"
        i += 1
        #print(region.nombre)


# CRISTHIAN GARCIA
# Generar modelo: Recibe un diccionario con las restricciones, una lista con n regiones y genera
# el modelo para minizinc.
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

    variables += "var int: Z;\n"
    kits_seguridad += " <= " + str(restricciones[KITS]) + ";\n"
    vacunacion += ")/10000 <= " + str(restricciones[VACUNACION]) + ";\n"
    costo_instalacion += ")/500000 <= " + str(restricciones[PRESUPUESTO]) + ";\n"
    cualificacion += " >= " + str(restricciones[CUALIFICACION]) + ";\n\n"
    solve = "solve maximize Z;\n"

    output += "];"

    return variables + kits_seguridad + vacunacion + costo_instalacion + cualificacion + no_negatividad + z + solve + output


def get_model(ruta_info, ruta_restricciones):
    # Para pruebas
    # regiones, restricciones = get_default_model()

    # Código que debería quedar
    regiones = load_info(ruta_info)
    restricciones = load_restric(ruta_restricciones)
    return regiones, generate_model(regiones, restricciones)


def init_solver(ruta_info="info.txt", ruta_restricciones="restricciones.txt"):
    gecode = Solver.lookup("coin-bc")    

    regiones, modelo = get_model(ruta_info, ruta_restricciones)

    trivial = Model()
    trivial.add_string(modelo)

    instance = Instance(gecode, trivial)

    # Encontrar todas las soluciones
    result = instance.solve(intermediate_solutions=False)
    #print(get_solution(result, regiones))


def get_solution(result, regiones):
    ans = ""
    ans += f"Z = {result.solution.objective}\n"

    for region in regiones:
        ans += f"{region.nombre} = {result[region.variable]}\n"
        # (region.variable, "=", result[region.variable])
    return ans

def init_solver2(regiones, restricciones):
    gecode = Solver.lookup("coin-bc")
    #gecode = Solver.lookup("gecode")

    modelo = generate_model(regiones, restricciones)
    print(modelo)

    trivial = Model()
    trivial.add_string(modelo)

    instance = Instance(gecode, trivial)

    # Encontrar todas las soluciones
    result = instance.solve(intermediate_solutions=False)
    r = get_solution(result, regiones)
    #print(r)
    return r

# init_solver()
