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

parser.add_argument("filein", help=".json file including the tree structure",
                    type=str)
parser.add_argument("fileout", help= "Output file with the new expressions")

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

variables_ordenadas = sorted(list(cjto_variables))

num_variables_por_monomio = [] # Para cada monomio, cuántas variables de cada contiene
for mon in lista_monomios:
    counts = []
    for var in cjto_variables:
        counts.append(mon.count("x_" + str(var)))
    num_variables_por_monomio.append(counts)

print("Combinaciones: " + str(combinaciones))
print("Variables por monomio: " + str(num_variables_por_monomio))

solver = Optimize()

expresiones = set() # Indexando obtienes la expresión i-ésima para luego reconstruir recursivamente
activas = []    
num_expresiones = len(combinaciones)
lista_combinaciones = list(combinaciones)

for i in range(len(combinaciones)):
    expresiones.add((i, ))

# Como máximo vas a tener que meter tantas variables como el mayor grado dentro del polinomio. SE PUEDE ACOTAR MÁS
# Primero se construyen todas las posibilidades. Otra opción es hacerlo dinámicamente

for i in range(3): # NUMERO AL AZAR EN PRINCIPIO - HEURÍSITICA LUEGO
    for r in range(2, maxDeg + 1):
        # Coge todas las anteriores
        for combo in itertools.combinations_with_replacement(range(num_expresiones), r): # Así combina e1*e1... en vez de x1*x1
            expresiones.add(tuple(sorted(combo)))

    num_expresiones = len(expresiones)

# Lista de tuplas. Para cada expresión, de cuáles depende
lista_expresiones = lista_expresiones = sorted(list(expresiones), key=lambda x: (len(x), x)) # Ordeno por primera componente

cuantas_originales = []
cuenta_activas = []

for i in range(num_expresiones):
    activas.append(Bool("act_" + str(i)))

    cuenta_activas.append(If(activas[i], 1, 0)) # Para contar cuántas hay activas

    # E5 = E1*E1. Solo se puede usar E5 si se usa también E1. Recursivamente se va expandiendo
    if i >= len(combinaciones): # No es una expresión del nivel 0
        for exp in lista_expresiones[i]:
            solver.add(Or(Not(activas[i]), activas[exp]))         # Implies(activas[i], activas[exp]))
            
        # El número de variables originales que contiene, es la suma de las que contienen las expresiones de las que depende
        cuantas = []
        for var in range(len(variables_ordenadas)):
            c = []
            cuantas.append(Int("cuantas_" + str(i) + "_" + str(var))) # La variable i cuántas variables var contiene
            # Para cada expresión de las que depende, cuántas apariciones de var tienen
            for exp in lista_expresiones[i]:
                c.append(cuantas_originales[exp][var])
                
            solver.add(cuantas[var] == addsum(c)) # Había un implies activa[i]
        
        cuantas_originales.append(cuantas)

    else: # Combinaciones iniciales
        cuantas = []
        for var in range(len(variables_ordenadas)):
            cuantas.append(Int("cuantas_" + str(i) + "_" + str(var))) # La variable i cuántas variables var contiene
            count = combo.count("x_" + str(var))

            solver.add(cuantas[var] == count)
        
        cuantas_originales.append(cuantas)

solver.add(addsum(cuenta_activas) <= max_intermedias)

grados_expresiones = []
for i in range(num_expresiones):
    grados_expresiones.append(Int("dege_" + str(i)))

    solver.add(grados_expresiones[i] <= maxDeg)
    solver.add(grados_expresiones[i] >= 0)

    grados = []
    if i < len(combinaciones):
        solver.add(grados_expresiones[i] == len(lista_combinaciones[i]))
    else:
        for exp in lista_expresiones[i]:
            grados.append(grados_expresiones[exp]) # ir sumando recursivo el grado de cada expresión de las que depende

        solver.add(grados_expresiones[i] == addsum(grados))

# Debe existir una combinación de las expresiones tal que consigan bajar el grado del monomio a maxDeg
for m in range(num_monomios):
    # Booleanos para indicar qué expresiones se usan para explicar el monomio m en concreto para poder diferenciar luego al hacer la suma
    selects = []  
    grado = []
    for exp in range(num_expresiones):
        b = Bool("select_" + str(m) + "_" + str(exp))
        selects.append(b)
        # Solo puedes seleccionar expresiones activas
        solver.add(Implies(b, activas[exp]))

        grado.append(If(selects[exp], 1, grados_expresiones[exp]))
    
    solver.add(addsum(grado) <= maxDeg)
    solver.add(addsum(grado) >= 0)

    # Ahora forzamos que el conjunto de expresiones seleccionadas coincida con el monomio
    # Para cada variable, si el monomio la contiene, la suma de las variables de las expresiones que contribuyen a la disminución de su
    # grado debe ser igual a las variables que tiene originalmente el monomio
    for var in range(len(variables_ordenadas)):
        suma = []
        for exp in range(num_expresiones):
            # If selected, cuenta esa cantidad de variable
            if num_variables_por_monomio[m][var] > 0: # Si el monomio contiene dicha variable
                suma.append(If(selects[exp], cuantas_originales[exp][var], 0))
        
        # Para cada variable del monomio, la suma de dicha variable de las expresiones que forman el monomio debe ser igual a las que había originalmente
        solver.add(addsum(suma) == num_variables_por_monomio[m][var])

    # Finalmente, al menos una expresión debe ser usada para cubrir el monomio
    solver.add(Or(selects))

# file.write(solver.to_smt2())
if solver.check() == sat:
    m = solver.model()

    for i in range(len(activas)):
        if is_true(m.eval(activas[i])):
            combo = expresiones[i]
            nombre_variable = "*".join(combo) # Convierte la tupla ('x_1', 'x_2') a "x_1*x_2"
            print(f"Variable intermedia seleccionada: {nombre_variable}")

else: print("unsat")

file.write(str(solver.assertions()))