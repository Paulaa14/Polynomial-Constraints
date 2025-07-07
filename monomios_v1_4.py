#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A partir de la versión entera, pasar a booleanos y añadir la idea de que una VI/monomio tiene para formarse, como máximo, maxDeg huecos que puede
# rellenar con otras VI, factores, o dejarlo vacío

# Se podría llevar guardado en un array el grado de cada expresión para no calcularlo todo el rato

from collections import defaultdict
import itertools
import json
from z3 import *
import argparse

def addsum(a):
    if len(a) == 0:
        return 0
    else:
        asum = a[0]
        for i in range(1,len(a)):
            asum = asum + a[i]
        return asum

def expand_factors(factors): # [x_1, x_1, x_2]
    expanded = []

    for f in factors:
        var = 'x_' + str(f["signal"])
        expanded.extend([var] * f["degree"])
    return expanded

def generate_combinations(expanded, maxDeg):
    combinaciones = set() # Conjunto para que no se repitan los elementos

    for r in range(1, min(maxDeg, len(expanded)) + 1): # Para que solo saque expresiones como mucho de maxDeg, el resto no me sirven como variables intermedias
        # combinations(p, r) -> tuplas de longitud r ordenadas y no repetidas de los elementos en p
        for combo in itertools.combinations(expanded, r):
            combinaciones.add(combo)

    return combinaciones

parser = argparse.ArgumentParser()

parser.add_argument("filein", help=".json file",
                    type=str)
parser.add_argument("fileout", help= "output file")

args=parser.parse_args()

f = open(args.filein)
data = json.load(f)

file = open(args.fileout, "w")

polinomios = data["polinomials"]
num_polinomios = data["num"]
maxDeg = data["degree"]
max_intermedias = 10

# Número de variables por nivel y número máximo de niveles, de momento los valores se ponen a mano
# num_niveles = 3
# num_variables_por_nivel = 2

degrees = [] # Cada monomio qué grado tiene
num_monomios = 0
combinaciones = set()
mayor_grado_polinomio = 0
cjto_variables = set()
lista_monomios = []

for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    for monomio in monomios:
        num_monomios += 1
        monomio["factors"] = sorted(monomio["factors"], key=lambda f: f["signal"])

        grado = sum(f["degree"] for f in monomio["factors"])
        degrees.append(grado)
        mayor_grado_polinomio = max(mayor_grado_polinomio, grado)

        for f in monomio["factors"]:
            cjto_variables.add(f["signal"])

        expanded = expand_factors(monomio["factors"])
        lista_monomios.append(expanded)

        cb = generate_combinations(expanded, maxDeg)
        combinaciones.update(cb)

if mayor_grado_polinomio <= maxDeg:
    sys.exit("No es necesario añadir ninguna variable auxiliar.")

cjto_variables = sorted(list(cjto_variables))
lista_combinaciones = sorted(list(combinaciones), key=str) # Ordenar por el toString de la combinación
num_combinaciones = len(lista_combinaciones)

num_variables_por_monomio = [] # Para cada monomio, cuántas variables de cada contiene
for mon in lista_monomios:
    counts = []
    for var in cjto_variables:
        counts.append(mon.count("x_" + str(var)))
    num_variables_por_monomio.append(counts)

    
num_variables_por_factor = [] # Para cada factor, cuántas variables de cada contiene
for comb in lista_combinaciones:
    counts = []
    for var in cjto_variables:
        counts.append(comb.count("x_" + str(var)))
    num_variables_por_factor.append(counts)

print("Combinaciones: " + str(lista_combinaciones))
print("Variables por monomio: " + str(num_variables_por_monomio))
print("Variables por factor: " + str(num_variables_por_factor))

solver = Solver()

num_niveles = max(1, int(math.ceil(math.log(mayor_grado_polinomio + 1, 2))))  # log base 2
num_variables_por_nivel = max(2, math.ceil(num_monomios))

activas = []
for nivel in range(num_niveles):
    variables_nivel = []
    for variable in range(num_variables_por_nivel):
        variables_nivel.append(Bool("x_" + str(nivel) + "_" + str(variable))) # Está activa la variable o no

    activas.append(variables_nivel)

ocupacion_huecos_variables = []

for nivel in range(num_niveles):
    huecos_nivel = []
    for variable in range(num_variables_por_nivel):
        huecos_var = []
        for hueco in range(maxDeg):
            ocupa = []

            if nivel > 0:
                for variable_nivel_anterior in range(num_variables_por_nivel):
                    ocupa.append(Bool("ocupav_" + str(nivel) + "_" + str(variable) + "_" + str(hueco) + "_" + str(variable_nivel_anterior)))

            for factor in range(num_combinaciones):
                ocupa.append(Bool("ocupaf_" + str(nivel) + "_" + str(variable) + "_" + str(hueco) + "_" + str(factor)))
            
            huecos_var.append(ocupa)
        
        huecos_nivel.append(huecos_var)
    
    ocupacion_huecos_variables.append(huecos_nivel)

# Orden dentro de los huecos -> Para todo hueco, los siguientes deben tener índice mayor. Todos los índices anteriores no deben estar activados
for nivel in range(num_niveles):
    for variable in range(num_variables_por_nivel):
        for hueco in range(maxDeg):

            idx = 0
            if nivel > 0:
                for variable_nivel_anterior in range(num_variables_por_nivel):
                    for hueco_sig in range(hueco + 1, maxDeg):
                        for variables_anteriores in range(0, idx):
                            solver.add(Implies(ocupacion_huecos_variables[nivel][variable][hueco][idx], Not(ocupacion_huecos_variables[nivel][variable][hueco_sig][variables_anteriores])))
                    
                    idx += 1
            
            for factor in range(num_combinaciones):
                for hueco_sig in range(hueco + 1, maxDeg):
                        for variables_anteriores in range(0, idx):
                            solver.add(Implies(ocupacion_huecos_variables[nivel][variable][hueco][idx], Not(ocupacion_huecos_variables[nivel][variable][hueco_sig][variables_anteriores])))
                
                idx += 1

for nivel in range(num_niveles):
    for variable in range(num_variables_por_nivel):
        cumple_grado = []
        variables_activas_por_var = []

        for hueco in range(maxDeg):
            variables_activas_por_hueco = []
            idx = 0
            if nivel > 0:
                for variable_nivel_anterior in range(num_variables_por_nivel):
                    # ocupa.append(Bool("ocupav_" + str(nivel) + "_" + str(variable) + "_" + str(hueco) + "_" + str(variable_nivel_anterior)))

                    solver.add(Implies(ocupacion_huecos_variables[nivel][variable][hueco][idx], activas[nivel - 1][variable_nivel_anterior]))

                    cumple_grado.append(If(ocupacion_huecos_variables[nivel][variable][hueco][idx], 1, 0))

                    variables_activas_por_hueco.append(If(ocupacion_huecos_variables[nivel][variable][hueco][idx], 1, 0))

                    idx += 1

            # La variable elem de nivel cuántas veces utiliza el factor fact
            for factor in range(num_combinaciones):
                cumple_grado.append(If(ocupacion_huecos_variables[nivel][variable][hueco][idx], len(lista_combinaciones[factor]), 0))

                variables_activas_por_hueco.append(If(ocupacion_huecos_variables[nivel][variable][hueco][idx], 1, 0))

                idx += 1

            # Puede dejarse vacío o ocuparse por 1 único elemento, ya sea VI o factor
            solver.add(addsum(variables_activas_por_hueco) <= 1)

            # Se oblga a rellenar los huecos de arriba a abajo, si un hueco está vacío, todos los siguientes también
            suma_actual = []
            suma_siguiente = []

            for hueco in range(maxDeg - 1):
                for var in ocupacion_huecos_variables[nivel][variable][hueco]:
                    suma_actual.append(If(var, 1, 0))

                for var in ocupacion_huecos_variables[nivel][variable][hueco + 1]:
                    suma_siguiente.append(If(var, 1, 0))

            solver.add(Implies(addsum(suma_actual) == 0, addsum(suma_siguiente) == 0))


            variables_activas_por_var.append(addsum(variables_activas_por_hueco))
        
        # La suma del grado de todo lo que se utiliza para formar la variable debe ser menor o igual que el grado máximo
        solver.add(addsum(cumple_grado) <= maxDeg) # Creo que OK porque no superan el grado

        # Eliminar variables que están formadas por una única variable intermedia/factor o por ninguna
        solver.add(addsum(variables_activas_por_var) > 1)


        # Todas las variables de un mismo nivel deben ser distintas, porque luego se da la opción de poder elegirla más de una vez en huecos distintos
        # Evitar duplicados entre variables del mismo nivel
        # Evitar duplicados ignorando el orden (conteo de dependencias)

        # Si se añade orden dentro de los huecos se puede simplificar
        for vi1 in range(num_variables_por_nivel):
            for vi2 in range(vi1 + 1, num_variables_por_nivel):
                diferencias = []
                
                rango = num_variables_por_nivel + num_combinaciones if nivel > 0 else num_combinaciones
                for idx in range(rango):
                    # Conteo en VI1
                    ocurrencias_vi1 = []
                    for hueco in range(maxDeg):
                        ocurrencias_vi1.append(If(ocupacion_huecos_variables[nivel][vi1][hueco][idx], 1, 0))
                    count_vi1 = addsum(ocurrencias_vi1)

                    # Conteo en VI2
                    ocurrencias_vi2 = []
                    for hueco in range(maxDeg):
                        ocurrencias_vi2.append(If(ocupacion_huecos_variables[nivel][vi2][hueco][idx], 1, 0))
                    count_vi2 = addsum(ocurrencias_vi2)

                    # Si la cuenta no coincide, lo anotamos como diferencia
                    diferencias.append(If(count_vi1 != count_vi2, 1, 0))

                # Si ambas VI están activas, deben diferir en al menos una dependencia (aunque en distinto orden)
                solver.add(Implies(And(activas[nivel][vi1], activas[nivel][vi2]), addsum(diferencias) > 0))

# Se cubren correctamente todas las variables originales en todas las variables intermedias
cuantas_variables = []

# Declaración
for nivel in range(num_niveles):
    cuantas_nivel = []
    for elem in range(num_variables_por_nivel):
        variables_elem = []
        for variable_original in range(len(cjto_variables)):
            variables_elem.append(Int("var_" + str(nivel) + "_" + str(elem) + "_" + str(variable_original)))
        
        cuantas_nivel.append(variables_elem)
    
    cuantas_variables.append(cuantas_nivel)

for nivel in range(num_niveles):
    for elem in range(num_variables_por_nivel):
        for variable_original in range(len(cjto_variables)):
            conteo_var = []
            for hueco in range(maxDeg):
                idx = 0
                if nivel > 0:
                    for var in range(num_variables_por_nivel):
                        # Si se ha utilizado en esta VI aporta las variables que contenga
                        conteo_var.append(If(ocupacion_huecos_variables[nivel][elem][hueco][idx], cuantas_variables[nivel - 1][var][variable_original], 0))
                        idx += 1

                for fact in range(num_combinaciones):
                    conteo_var.append(If(ocupacion_huecos_variables[nivel][elem][hueco][idx], num_variables_por_factor[fact][variable_original], 0))
                    idx += 1
                        
            solver.add(cuantas_variables[nivel][elem][variable_original] == addsum(conteo_var))

# Los monomios resultantes cumplen todos 0 <= grado <= maxDeg
ocupacion_huecos_monomios = []

for mon in range(num_monomios):
    huecos_monomio = []

    for hueco in range(maxDeg):
        ocupa = []
        if num_niveles > 0:
            for variable in range(num_variables_por_nivel):                
                ocupa.append(Bool("ocupamv_" + str(mon) + "_" + str(hueco) + "_" + str(variable)))

        for factor in range(num_combinaciones):
            ocupa.append(Bool("ocupamf_" + str(mon) + "_" + str(factor)))

        huecos_monomio.append(ocupa)
    
    ocupacion_huecos_monomios.append(huecos_monomio)

# Orden dentro de los huecos -> Para todo hueco, los siguientes deben tener índice mayor. Todos los índices anteriores no deben estar activados
for mon in range(num_monomios):
    for hueco in range(maxDeg):

        idx = 0
        if num_niveles > 0:
            for variable_nivel_anterior in range(num_variables_por_nivel):
                for hueco_sig in range(hueco + 1, maxDeg):
                    for variables_anteriores in range(0, idx):
                        solver.add(Implies(ocupacion_huecos_monomios[mon][hueco][idx], Not(ocupacion_huecos_monomios[mon][hueco_sig][variables_anteriores])))
                
                idx += 1
        
        for factor in range(num_combinaciones):
            for hueco_sig in range(hueco + 1, maxDeg):
                    for variables_anteriores in range(0, idx):
                        solver.add(Implies(ocupacion_huecos_monomios[mon][hueco][idx], Not(ocupacion_huecos_monomios[mon][hueco_sig][variables_anteriores])))
            
            idx += 1

for mon in range(num_monomios):
    de_cuantas_depende = []

    for hueco in range(maxDeg):
        activos_hueco = []
        idx = 0
        if num_niveles > 0:
            for variable in range(num_variables_por_nivel):                

                solver.add(Implies(ocupacion_huecos_monomios[mon][hueco][idx], activas[num_niveles - 1][variable]))

                de_cuantas_depende.append(If(ocupacion_huecos_monomios[mon][hueco][idx], 1, 0))
                activos_hueco.append(If(ocupacion_huecos_monomios[mon][hueco][idx], 1, 0))

                idx += 1

        for factor in range(num_combinaciones):

            de_cuantas_depende.append(If(ocupacion_huecos_monomios[mon][hueco][idx], len(lista_combinaciones[factor]), 0))
            activos_hueco.append(If(ocupacion_huecos_monomios[mon][hueco][idx], 1, 0))

            idx += 1
        
        solver.add(addsum(activos_hueco) <= 1)

        # Se oblga a rellenar los huecos de arriba a abajo, si un hueco está vacío, todos los siguientes también
        suma_actual = []
        suma_siguiente = []

        for hueco in range(maxDeg - 1):
            for var in ocupacion_huecos_monomios[mon][hueco]:
                suma_actual.append(If(var, 1, 0))

            for var in ocupacion_huecos_monomios[mon][hueco + 1]:
                suma_siguiente.append(If(var, 1, 0))

        solver.add(Implies(addsum(suma_actual) == 0, addsum(suma_siguiente) == 0))

    # SUMA DE LAS LONGITUDES DE LAS EXPRESIONES DE LAS QUE DEPENDE
    solver.add(addsum(de_cuantas_depende) <= maxDeg) # NO ES TRIVIAL por contrucción porque al poder meter factores, el grado aumenta

# Se cubren todas las variables originales que tiene el monomio
for mon in range(num_monomios):
    for var in range(len(cjto_variables)):
        conteo_var = []
        for hueco in range(maxDeg):
            ocupa = ocupacion_huecos_monomios[mon][hueco]
            idx = 0

            if num_niveles > 0:
                for elem in range(num_variables_por_nivel):
                    conteo_var.append(If(ocupa[idx], cuantas_variables[num_niveles - 1][elem][var], 0))
                    idx += 1

            for fact in range(num_combinaciones):
                conteo_var.append(If(ocupa[idx], num_variables_por_factor[fact][var], 0))
                idx += 1

        solver.add(addsum(conteo_var) == num_variables_por_monomio[mon][var])

cuentan = []
suma_cuentan = []

# Se utiliza en la variable y el número de huecos ocupados es mayor que 1
for nivel in range(num_niveles):
    cuentan_nivel = []
    for elem in range(num_variables_por_nivel):
        cuentan_nivel.append(Bool("cuenta_" + str(nivel) + "_" + str(elem)))
    
    cuentan.append(cuentan_nivel)

# Solo para las variables
for nivel in range(num_niveles - 1):
    for elem in range(num_variables_por_nivel):
        huecos_ocupados = []
        for variable_siguiente_nivel in range(num_variables_por_nivel):
            depende = []
            for hueco in range(maxDeg):
                for aux in range(num_variables_por_nivel):
                    huecos_ocupados.append(If(ocupacion_huecos_variables[nivel + 1][variable_siguiente_nivel][hueco][aux], 1, 0))
                    # Ver si se utiliza variable_siguiente_nivel depende de elem en algún hueco
                    if aux == elem: depende.append(ocupacion_huecos_variables[nivel + 1][variable_siguiente_nivel][hueco][elem])
                
                for fact in range(num_combinaciones):
                    huecos_ocupados.append(If(ocupacion_huecos_variables[nivel + 1][variable_siguiente_nivel][hueco][fact], 1, 0))

            solver.add(Implies(And(addsum(huecos_ocupados) > 1, Or(*depende), activas[nivel][elem]), cuentan[nivel][elem]))

for mon in range(num_monomios):
    for elem in range(num_variables_por_nivel):
        for hueco in range(maxDeg):
            solver.add(Implies(And(activas[num_niveles - 1][elem], ocupacion_huecos_monomios[mon][elem][hueco]), cuentan[num_niveles - 1][elem]))

for nivel in range(num_niveles):
    for elem in range(num_variables_por_nivel):
        suma_cuentan.append(If(cuentan[nivel][elem], 1, 0))

solver.add(addsum(suma_cuentan) <= max_intermedias)


# for nivel in range(num_niveles):
#     for elem in range(num_variables_por_nivel):
#         c = Bool("cuenta_" + str(nivel) + "_" + str(elem))
#         suma_cuentan.append(If(c, 1, 0))
#         cuentan.append(c)
#         activas_sig_nivel = []
#         if nivel < num_niveles - 1:
#             # Hay alguna variable del siguiente nivel que tiene otra dependencia con un elemento de mi nivel que no es el elemento que estoy mirando
#             for aux in range(num_variables_por_nivel):
#                 auxiliar = []
#                 for hueco in range(maxDeg):
#                     # if nivel < num_niveles - 1:
#                     num_veces_consigo_misma = 0
#                     for var in range(num_variables_por_nivel):
#                         if var != elem and num_veces_consigo_misma > 0:
#                             auxiliar.append(If(ocupacion_huecos_variables[nivel + 1][aux][hueco][var], 1, 0))
#                         else: num_veces_consigo_misma += 1
                    
#                     for fact in range(num_combinaciones):
#                         auxiliar.append(If(ocupacion_huecos_variables[nivel + 1][aux][hueco][num_variables_por_nivel + fact], 1, 0))
#                     # else: 
#                     #     for fact in range(num_combinaciones):
#                     #         auxiliar.append(If(ocupacion_huecos_variables[nivel + 1][aux][hueco][fact], 1, 0))

#                 # Tiene activas tanto elem como aux y tener dependencia aux con elem
#                 aux_depende_de_elem = [] # Ver si existe dependencia entre aux y elem
#                 for hueco in range(maxDeg):
#                     aux_depende_de_elem.append(If(ocupacion_huecos_variables[nivel + 1][aux][hueco][elem], 1, 0))

#                 activas_sig_nivel.append(If(And(addsum(auxiliar) > 0, addsum(aux_depende_de_elem) > 0, activas[nivel + 1][aux]), 1, 0))
            
#             solver.add(Implies(And(activas[nivel][elem], addsum(activas_sig_nivel) > 0), c))
#             solver.add(c == And(activas[nivel][elem], addsum(activas_sig_nivel) > 0))
        
#         else:
#             # En el último nivel si está activa, cuenta si la utiliza un monomio
#             for mon in range(num_monomios):
#                 for hueco in range(maxDeg):          
#                     # solver.add(Implies(And(activas[nivel][elem], ocupacion_huecos_monomios[mon][hueco][elem]), c)) 
#                     solver.add(c == And(activas[nivel][elem], ocupacion_huecos_monomios[mon][hueco][elem]))          

# solver.add(addsum(suma_cuentan) <= max_intermedias)

if solver.check() == sat:
    m = solver.model()

    print("\n=== Variables Intermedias Activas y sus Dependencias ===\n")
    for nivel in range(num_niveles):
        for elem in range(num_variables_por_nivel):
            var_activa = activas[nivel][elem]
            if is_true(m.eval(var_activa)):
                print(f"🔹 VI(n{nivel}, v{elem}) está activa y depende de:")

                for hueco in range(maxDeg):
                    ocupacion = ocupacion_huecos_variables[nivel][elem][hueco]

                    for i, var in enumerate(ocupacion):
                        if is_true(m.eval(var)):
                            if nivel > 0 and i < num_variables_por_nivel:
                                print(f"  - Hueco {hueco}: VI(n{nivel - 1}, v{i})")
                            else:
                                # i - offset para obtener índice de factor
                                factor_index = i - (num_variables_por_nivel if nivel > 0 else 0)
                                print(f"  - Hueco {hueco}: Factor {lista_combinaciones[factor_index]}")
    
    print("\n=== Monomios Reconstruidos ===\n")
    for mon in range(num_monomios):
        print(f"🔸 Monomio {mon} depende de:")
        for hueco in range(maxDeg):
            ocupacion = ocupacion_huecos_monomios[mon][hueco]

            for i, var in enumerate(ocupacion):
                if is_true(m.eval(var)):
                    if i < num_variables_por_nivel:
                        print(f"  - Hueco {hueco}: VI(n{num_niveles - 1}, v{i})")
                    else:
                        factor_index = i - num_variables_por_nivel
                        print(f"  - Hueco {hueco}: Factor {lista_combinaciones[factor_index]}")

else:
    print("\n❌ No se ha encontrado una solución.")

# file.write(str(solver.assertions()))

with open("debug_constraints.smt2", "w") as out:
    out.write(solver.to_smt2())