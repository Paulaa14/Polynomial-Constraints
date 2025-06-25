#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import itertools
import json
from z3 import *
import argparse

def addsum(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else :
        x = a.pop()
        return x + addsum(a)

def addexists(a):
    if len(a) == 0:
        return False
    elif len(a) == 1:
        return a[0]
    else :
        x = a.pop()
        return Or(x,addexists(a))

def expand_factors(factors): # [x_1, x_1, x_2]
    expanded = []

    for f in factors:
        var = 'x_' + str(f["signal"])
        expanded.extend([var] * f["degree"])
    return expanded

def generate_combinations(factors, maxDeg):
    expanded = expand_factors(factors)
    combinaciones = set() # Conjunto para que no se repitan los elementos

    for r in range(1, min(maxDeg, len(expanded)) + 1): # Para que solo saque expresiones como mucho de maxDeg, el resto no me sirven como variables intermedias
        # combinations(p, r) -> tuplas de longitud r ordenadas y no repetidas de los elementos en p
        for combo in itertools.combinations(expanded, r):
            combinaciones.add(combo)

    return combinaciones

def count_combinations(monomios, maxDeg):
    combinaciones = set()

    for monomio in monomios:
        combs = generate_combinations(monomio["factors"], maxDeg)
        for c in combs:
            if len(c) > 1: combinaciones.add(tuple(sorted(c)))
    return combinaciones

# Una lista está contenida dentro de otra
def contains(variables, target):
    vars_copy = list(variables)  # Copia para no modificar la original
    for t in target:
        if t in vars_copy:
            vars_copy.remove(t)  # Quitamos uno a uno cada coincidencia
        else:
            return False
    return True


parser = argparse.ArgumentParser()

parser.add_argument("filein", help=".json file including the tree structure",
                    type=str)
parser.add_argument("fileout", help= "Output file with the new expressions")

args=parser.parse_args()

f = open(args.filein)
data = json.load(f)

file = open(args.fileout, "w")

polinomios = data["polinomials"]
num_polinomios = data["num"]
maxDeg = data["degree"] # Luego leerlo del fichero
# num_intermedias = 3 # Número máximo de variables intermedias que se permiten

degrees = [] # Cada monomio qué grado tiene
num_monomios = 0
combinaciones = set()
mayor_grado_polinomio = 0

count = 0 # Para cuando hay más de un polinomio
for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    num_monomios += len(monomios)

    for i in range(len(monomios)):
        # Ordenar por el valor de signal para que xy == yx
        monomios[i]["factors"] = sorted(monomios[i]["factors"], key=lambda f: f["signal"])

        degrees.append(0)
        for f in monomios[i]["factors"]: # Al ser un producto se suma
            degrees[count] = degrees[count] + f["degree"]

        mayor_grado_polinomio = max(mayor_grado_polinomio, degrees[count])
        count = count + 1

    # Todas las posibles subexpresiones que aparecen en los monomios y el número de veces que aparece cada una
    cb = count_combinations(monomios, maxDeg)

    for c in cb:
        combinaciones.add(c)


print(combinaciones)
if mayor_grado_polinomio <= maxDeg:
    sys.exit("No es necesario añadir ninguna variable auxiliar.")

solver = Optimize()

grados_monomios = [] # Para cada monomio, qué grado tiene. Ya sea originalmente o tras hacer alguna sustitución.

for i in range(num_monomios):
    grados_monomios.append(Int("degm_" + str(i)))

    solver.add(grados_monomios[i] >= 0)
    solver.add(grados_monomios[i] <= maxDeg)

# Con los factores de nivel 0 puedes escoger cualquiera, las variables intermedias solo puedes utilizar las que estén activas
# Booleanos para ver qué monomios ya tienen grado <= maxDeg. Cuando todos estén a cierto se para de buscar variables y de subir niveles

expresiones = set() # Indexando obtienes la expresión i-ésima para luego reconstruir recursivamente
activas = []

num_expresiones = len(combinaciones)
lista_combinaciones = list(combinaciones)

for i in range(num_expresiones):
    expresiones.add((i, )) # Añadir x1 como VI no tiene sentido

# Como máximo vas a tener que meter tantas variables como el mayor grado dentro del polinomio. SE PUEDE ACOTAR MÁS
# Primero se construyen todas las posibilidades. Otra opción es hacerlo dinámicamente
for i in range(int(mayor_grado_polinomio.bit_length())): # AJUSTAR. Coge log2(maxGrado)
    for r in range(2, maxDeg + 1):
        # Coge todas las anteriores
        for combo in itertools.product(range(num_expresiones), repeat = r): # Así combina e1*e1... en vez de x1*x1
            expresiones.add(tuple(sorted(combo)))

    num_expresiones = len(expresiones)

expresiones = sorted(expresiones, key=lambda x: (x[0], x[1] if len(x) > 1 else -1))
lista_expresiones = list(expresiones) # Lista de tuplas

for i in range(len(lista_expresiones)):
    activas.append(Bool("act_" + str(i)))

    solver.add_soft(Not(activas[i]), 1, id = "activas") # Minimiza el número de variables intermedias

# E5 = E1*E1. Solo se puede usar E5 si se usa también E1. Recursivamente se va haciendo
for i in range(len(lista_expresiones)):
    if i >= len(combinaciones): # No es una expresión del nivel 0
        for exp in lista_expresiones[i]:
            solver.add(Implies(activas[i], activas[exp]))

def reconstruir_expresiones(id, reconstrucciones):
    if id < len(reconstrucciones): # Ya está calculado
        return reconstrucciones[id]
    else:
        expresion = []
        for e in lista_expresiones[id]:
            expr = reconstruir_expresiones(e, reconstrucciones)
            for elem in expr: expresion.append(elem)
        return expresion

# Reconstruir variables intermedias creadas
reconstrucciones = []
for i in range(len(lista_expresiones)):
    if i < len(combinaciones): reconstrucciones.append(list(lista_combinaciones[i]))
    else: 
        expr = reconstruir_expresiones(i, reconstrucciones)
        reconstrucciones.append(expr) # Poco eficiente porque igual reconstruyes cosas que no son necesarias

grados = []
for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    for i in range(len(monomios)):
        deg = []
        f = expand_factors(monomios[i]["factors"])

        # Sólo si la contiene y el keep está a true entonces el grado se modifica. 
        # Recorro al revés para sustituir primero las expresiones más grandes
        for e in range(len(reconstrucciones) - 1, -1, -1):
            if contains(f, reconstrucciones[e]):
                deg.append(If(activas[e], len(reconstrucciones[e]) - 1, 0))

                # Elimino los elementos de f porque ya han sido sustituidos
                for item in reconstrucciones[e]:
                    f.remove(item)

        grados.append(deg)
        
for i in range(num_monomios):
    solver.add(grados_monomios[i] == degrees[i] - addsum(grados[i]))


if solver.check() == sat:
    m = solver.model()

    for i in range(len(activas)):
        if is_true(m.eval(activas[i])):
            combo = reconstrucciones[i]
            nombre_variable = "*".join(combo) # Convierte la tupla ('x_1', 'x_2') a "x_1*x_2"
            print(f"Variable intermedia seleccionada: {nombre_variable}")

else: print("unsat")

# print(solver.assertions())
# file.write(solver.to_smt2())