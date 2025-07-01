#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    for r in range(2, min(maxDeg, len(expanded)) + 1): # Para que solo saque expresiones como mucho de maxDeg, el resto no me sirven como variables intermedias
        # combinations(p, r) -> tuplas de longitud r ordenadas y no repetidas de los elementos en p
        for combo in itertools.combinations(expanded, r):
            combinaciones.add(combo)

    return combinaciones

# def count_combinations(monomios, maxDeg, factores): # Cada combinación cuántas veces aparece
#     combinaciones = set()
#     for monomio in monomios:
#         combs = generate_combinations(monomio["factors"], maxDeg, factores)
#         for c in combs:
#             if len(c) > 1: combinaciones.add(tuple(sorted(c)))
#     return combinaciones

# Una lista está contenida dentro de otra
def contains(variables, target):
    vars_copy = list(variables)  # Copia para no modificar la original
    for t in target:
        if t in vars_copy:
            vars_copy.remove(t) 
        else:
            return False
    return True

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
max_intermedias = 3

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
lista_combinaciones = list(combinaciones)
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

print("Combinaciones: " + str(combinaciones))
print("Variables por monomio: " + str(num_variables_por_monomio))
print("Variables por factor: " + str(num_variables_por_factor))

solver = Solver()

# Número de variables por nivel y número máximo de niveles, de momento a mano
num_niveles = 3
num_variables_por_nivel = 10

# Matriz, para cada nivel, las variables que contiene
variables_intermedias = []
activas = []

for nivel in range(num_niveles):
    variables_nivel = []
    for elem in range(num_variables_por_nivel):
        variables_nivel.append(Bool("x_" + str(nivel) + "_" + str(elem))) # Está activa la variable o no
        activas.append(If(variables_nivel[elem], 1, 0))

    variables_intermedias.append(variables_nivel)

# De momento, cada nivel se forma con variables del nivel inmediatamente anterior y factores iniciales
dependencias = []
for nivel in range(num_niveles):
    deps_nivel = []
    for elem in range(num_variables_por_nivel):
        deps_var = []
        cumple_grado = []
        cumple_var = []

        if nivel > 0:
            # La variable elem de nivel utiliza o no la variable var del nivel anterior
            for var in range(num_variables_por_nivel):
                deps_var.append(Bool("depv_" + str(nivel) + "_" + str(elem) + "_" + str(var))) 

                # Solo se puede utilizar si var está activa
                solver.add(Implies(deps_var[var], variables_intermedias[nivel - 1][var]))

                # Si se utiliza esta variable de otro nivel, su grado es 1, sino 0
                cumple_grado.append(If(deps_var[var], 1, 0))

        # La variable elem de nivel utiliza o no el factor fact
        for fact in range(num_combinaciones):
            elem = Bool("depf_" + str(nivel) + "_" + str(elem) + "_" + str(fact))
            deps_var.append(elem)

            # Si se utiliza, su grado es el del factor ya que se va a sustituir
            cumple_grado.append(If(elem, len(lista_combinaciones[fact]), 0))

        # La suma del grado de todo lo que se utiliza para formar la variable debe ser menor o igual que el grado máximo
        solver.add(addsum(cumple_grado) <= maxDeg)

        deps_nivel.append(deps_var)
    
    dependencias.append(deps_nivel)

deps_monomios = []
for mon in range(num_monomios):
    deps_var = []
    cumple_grado = []

    if num_niveles > 0:
        for var in range(num_variables_por_nivel):
            deps_var.append(Bool("depmv_" + str(mon) + "_" + str(var)))

            # Solo se puede utilizar si var está activa
            solver.add(Implies(deps_var[var], variables_intermedias[num_niveles - 1][var]))

            cumple_grado.append(If(deps_var[var], 1, 0))

    for fact in range(num_combinaciones):
        elem = Bool("depmf" + str(mon) + "_" + str(fact))
        deps_var.append(elem)
        cumple_grado.append(If(elem, 1, 0))

    deps_monomios.append(deps_var)

    solver.add(addsum(cumple_grado) <= maxDeg)

# Se cubren correctamente todas las variables en todas las variables intermedias
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
            if nivel > 0:
                for var in range(num_variables_por_nivel):
                    # Si se ha utilizado en esta VI aporta las variables que contenga
                    conteo_var.append(If(dependencias[nivel][elem][var], cuantas_variables[nivel - 1][var][variable_original], 0))
                
                for fact in range(num_combinaciones):
                    conteo_var.append(If(dependencias[nivel][elem][num_variables_por_nivel + fact], num_variables_por_factor[fact][variable_original], 0))    
                    
            else: 
                for fact in range(num_combinaciones):
                    conteo_var.append(If(dependencias[nivel][elem][fact], num_variables_por_factor[fact][variable_original], 0))    
                 
            solver.add(cuantas_variables[nivel][elem][variable_original] == addsum(conteo_var))

for mon in range(num_monomios):
    for var in range(len(cjto_variables)):
        conteo_var = []
        if num_niveles > 0:
            for elem in range(num_variables_por_nivel):
                conteo_var.append(If(deps_monomios[mon][elem], cuantas_variables[num_niveles - 1][elem][variable_original], 0))
        
            for fact in range(num_combinaciones):
                conteo_var.append(If(deps_monomios[mon][num_variables_por_nivel + fact], num_variables_por_factor[fact][var], 0))

        else:
            for fact in range(num_combinaciones):
                conteo_var.append(If(deps_monomios[mon][fact], num_variables_por_factor[fact][var], 0))

        solver.add(addsum(conteo_var) == num_variables_por_monomio[mon][var])

# cuentan_como_activas = []

# for nivel in range(num_niveles):
#     for elem in range(num_variables_por_nivel):
#         vi = variables_intermedias[nivel][elem]  # La variable booleana: si está activa o no
#         deps = dependencias[nivel][elem]  # Lista de dependencias (otras variables y factores)

#         # Creamos una lista de condiciones: cada una es "esta dependencia está activa"
#         usos = []
#         for d in deps:
#             usos.append(If(d, 1, 0))

#         # Suma de variables usadas en esta expresión
#         total_usadas = addsum(usos)

#         # Solo cuenta como activa si se usa y además se usa junto a alguna otra
#         # (es decir, total_usadas >= 2)
#         usada_con_otra = And(vi, total_usadas >= 2)

#         cuentan_como_activas.append(If(usada_con_otra, 1, 0))


# solver.add(addsum(cuentan_como_activas) <= max_intermedias)

# file.write(solver.to_smt2())
if solver.check() == sat:
    m = solver.model()
    print("\n=== Variables intermedias seleccionadas ===\n")
    
    for nivel in range(num_niveles):
        for elem in range(num_variables_por_nivel):
            var_activa = variables_intermedias[nivel][elem]
            if is_true(m.eval(var_activa)):
                print(f"Nivel {nivel}, Variable {elem}:")

                deps = dependencias[nivel][elem]
                usados = []
                
                # Variables del nivel anterior (si existen)
                if nivel > 0:
                    for var_prev in range(num_variables_por_nivel):
                        dep = deps[var_prev]
                        if is_true(m.eval(dep)):
                            usados.append(f"VI(n{nivel-1},v{var_prev})")

                # Combinaciones base
                offset = 0 if nivel == 0 else num_variables_por_nivel
                for fact in range(num_combinaciones):
                    dep_idx = offset + fact
                    dep = deps[dep_idx]
                    if is_true(m.eval(dep)):
                        usados.append("*".join(lista_combinaciones[fact]))

                print("  → Compuesta por:", ", ".join(usados))
else:
    print("UNSAT: No se encontró solución.")

# file.write(str(solver.assertions()))

with open("debug_constraints.smt2", "w") as out:
    out.write(solver.to_smt2())