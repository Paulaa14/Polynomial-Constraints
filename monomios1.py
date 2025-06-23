#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Primero como un problema SAT, puedo resolverlo con 2 variables intermedias? 3? Teniendo como grado máximo permitido 2 por ejemplo.
# Aparecen muchas simetrías de soluciones que solamente se diferencian en el renombrado de las variables. Se pueden controlar numerando u ordenando.

from collections import Counter, defaultdict
import itertools

def addsum(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else :
        x = a.pop()
        return x + addsum(a) 

def expand_factors(factors): # [x_1, x_1, x_2]
    expanded = []

    for f in factors:
        var = 'x_' + str(f["signal"])
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

# Una lista está contenida dentro de otra
def contiene_variables(variables, target):
    return not (Counter(target) - Counter(variables))

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

degrees = [] # Cada monomio qué grado tiene

for i in range(num_monomios):
    # Ordenar por el valor de signal para que xy == yx
    monomios[i]["factors"] = sorted(monomios[i]["factors"], key=lambda f: f["signal"])

    degrees.append(0)
    for f in monomios[i]["factors"]:
        degrees[i] = degrees[i] + f["degree"]


# Todas las posibles subexpresiones que aparecen en los monomios y el número de veces que aparece cada una
combinaciones = count_combinations(monomios, maxDeg)

print(combinaciones)

# Ordeno de manera descendiente por el segundo valor que indica el número de veces que aparece cada combinación
# combinaciones = sorted(combinaciones.items(), key=lambda item: item[1], reverse=True)

solver = Optimize()

# Tener una lista con las posibles combinaciones de variables y las que más conviene quedarse son las que más aparecen

# Variables Z3
grados_monomios = [] # Para cada monomio, qué grado tiene. Ya sea originalmente o tras hacer alguna sustitución.
keeps = [] # Como máximo puede haber num_intermedias VI, pero puede haber menos. Obligo a que estén las primeras en el array
# Otra opción es tener un array del mismo tamaño que el array de las combinaciones de las variables con los booleanos 
# para cada una y el número de keeps debe ser <= num_intermedias

for i in range(num_monomios):
    grados_monomios.append(Int("degm_" + str(i)))

    solver.add(grados_monomios[i] >= 0)
    solver.add(grados_monomios[i] <= maxDeg)
    # solver.add(grados_monomios[i] <= degrees[i]) # El grado tiene que ser menor o igual que el grado original

combinaciones_lista = list(combinaciones.keys())

k = []
for i in range(len(combinaciones)):
    keeps.append(Bool("keep_" + str(i)))

    solver.add_soft(Not(keeps[i]), 1, id = "keeps") # Minimiza el número de variables intermedias
    solver.add_soft(keeps[i], combinaciones[combinaciones_lista[i]], id = "apariciones") # Hace que se prioricen las VI que aparecen más veces

    k.append(If(keeps[i], 1, 0))

solver.add(addsum(k) <= num_intermedias) # El número de variables intermedias debe ser menor o igual que el valor máximo permitido

for i in range(num_monomios):
    deg = []
    f = expand_factors(monomios[i]["factors"])
    for j in range(len(combinaciones_lista)):
        if contiene_variables(f, list(combinaciones_lista[j])):
            deg.append(If(keeps[j], len(combinaciones_lista[j]) - 1, 0))
    solver.add(grados_monomios[i] == degrees[i] - addsum(deg))


if solver.check() == sat:
    m = solver.model()

    for i in range(len(keeps)):
        if is_true(m.eval(keeps[i])):
            combo = combinaciones_lista[i]
            nombre_variable = "*".join(combo) # Convierte la tupla ('x_1', 'x_2') a "x_1*x_2"
            print(f"Variable intermedia seleccionada: {nombre_variable}")

else: print("unsat")

# print(solver.assertions())
# print(solver.model())