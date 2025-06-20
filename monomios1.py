#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Primero como un problema SAT, puedo resolverlo con 2 variables intermedias? 3? Teniendo como grado máximo permitido 2 por ejemplo.
# Aparecen muchas simetrías de soluciones que solamente se diferencian en el renombrado de las variables. Se pueden controlar numerando u ordenando.

from collections import defaultdict
import itertools


def expand_factors(factors): # [x_1, x_1, x_2]
    expanded = []
    for f in factors:
        var = f"x_{f['signal']}"
        expanded.extend([var] * f["degree"])
    return expanded

def generate_combinations(factors, maxDeg):
    expanded = expand_factors(factors)
    combinaciones = set() # Conjunto para que no se repitan los conjuntos

    for r in range(1, min(maxDeg, len(expanded)) + 1): # Para que solo saque expresiones como mucho de maxDeg, el resto no me sirven como variables intermedias
        # combinations(p, r) -> tuplas de longitud r ordenadas y no repetidas de los elementos en p
        for combo in itertools.combinations(expanded, r):
            combinaciones.add(combo)
    
    return combinaciones

def count_combinations(monomios, maxDeg):
    mapa = defaultdict(int) # Cada subexpresión en cuántos monomios aparece

    for monomio in monomios:
        combs = generate_combinations(monomio["factors"], maxDeg)

        for c in (combs):
            mapa[c] += 1 # Sumas 1 en las subexpresiones que están en el monomio

    return mapa

import json
from z3 import *

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("filein", help=".json file including the tree structure",
                    type=str)
parser.add_argument("fileout", help= "Output file with the new expressions")


args=parser.parse_args()

f = open(args.filein)
data = json.load(f)

file = open(args.fileout, "w")

monomios = data["monomials"]
maxDeg = 2 # Luego leerlo del fichero
num_intermedias = 3 # Número máximo de variables intermedias que se permiten
num_monomios = len(monomios)

# Todas las posibles subexpresiones que aparecen en los monomios y el número de veces que aparece cada una
combinaciones = count_combinations(monomios, maxDeg)

print(combinaciones)

# Procesado de la entrada

# lista_variables = [] # Variables que se tienen para añadir todas las combinaciones
# combinaciones = map() # Mapa para cada subexpresión cuántas veces aparece

# for m in (num_monomios):
#     factores = monomios[m]["factors"]

#     for f in (len(factores)): # Cada señal

#         indice = factores["signal"]
#         señal = "x_" + indice # x1, x2...

#         # if not(señal in lista_variables):
#         #    lista_variables.append(señal)
#         for a in range(min(factores["degree"], maxDeg)): # Añadir x1, x1^2, x1^3...., x1^maxDeg
#             x = ""
#             for i in range(a):
#                 x += señal
#             combinaciones[x] = combinaciones[x] + 1 # Hay una nueva aparición de dicha subexpresión

        # Para toda variable dentro del monomio se añade la combinación con ella
#         for s in (len(factores)):
#             if indice != factores[s]:

    
    

solver = Solver()

# Tener una lista con las posibles combinaciones de variables y las que más conviene quedarse son las que más aparecen

# Variables Z3
grados_monomios = [] # Para cada monomio, qué grado tiene. Ya sea originalmente o tras hacer alguna sustitución.
grados_intermedias = [] # Cada variable intermedia, qué grado tiene. Elegir de las combinaciones, cuáles coges y cuáles no.
keeps = [] # Como máximo puede haber num_intermedias VI, pero puede haber menos. Obligo a que estén las primeras en el array
# Otra opción es tener un array del mismo tamaño que el array de las combinaciones de las variables con los booleanos 
# para cada una y el número de keeps debe ser <= num_intermedias

for i in range(num_monomios):
    grados_monomios.append(Int("degm_" + str(i)))

    solver.add(grados_monomios[i] >= 0)
    solver.add(grados_monomios[i] <= maxDeg)

for i in range(num_intermedias):
    grados_intermedias.append(Int("degi_" + str(i)))
    keeps.append(Bool("keep_" + str(i)))

    solver.add(grados_intermedias[i] >= 0)
    solver.add(grados_intermedias[i] <= maxDeg)

for i in range(num_intermedias - 1): 
    # Si keeps[i] está a falso, todas las demás tienen que estarlo, así obligo a que se quede las primeras variables
    solver.add(Or(keeps[i], Not(keeps[i + 1])))
