#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    return (combinaciones, expanded)

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

count = 0 # Para cuando hay más de un polinomio
factores = []
for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    lista_monomios.append(monomios)
    num_monomios += len(monomios)

    for i in range(len(monomios)):
        # Ordenar por el valor de signal para que xy == yx
        monomios[i]["factors"] = sorted(monomios[i]["factors"], key=lambda f: f["signal"])

        degrees.append(0)
        for f in monomios[i]["factors"]: # Al ser un producto se suma
            degrees[count] = degrees[count] + f["degree"]
            cjto_variables.add(f["signal"])

        mayor_grado_polinomio = max(mayor_grado_polinomio, degrees[count])
        count = count + 1

        fact = []
        (cb, fact) = generate_combinations(monomios[i]["factors"], maxDeg)
        factores.append(fact)

        for c in cb:
            combinaciones.add(c)

num_variables_por_monomio = []
for m in range(num_monomios): # Para cada monomio, cuántas variables de cada una contiene
    num = []
    for var in range(len(cjto_variables)):
        cont = 0
        for elem in monomios[m]:
            if elem == var:
                cont += 1
        num.append(cont)

    num_variables_por_monomio.append(num)

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

expresiones = sorted(expresiones, key=lambda x: (x[0], x[1] if len(x) > 1 else -1))
lista_expresiones = list(expresiones) # Lista de tuplas. Para cada expresión, de cuáles depende
cuantas_originales = []

cuenta_activas = []
for i in range(num_expresiones):
    activas.append(Bool("act_" + str(i)))

    If(activas[i], 1, 0) # Para contar cuántas hay activas

    # E5 = E1*E1. Solo se puede usar E5 si se usa también E1. Recursivamente se va expandiendo
    if i >= len(combinaciones): # No es una expresión del nivel 0
        for exp in lista_expresiones[i]:
            solver.add(Or(Not(activas[i]), activas[exp]))         # Implies(activas[i], activas[exp]))
            
        # Las variables originales que contiene es la suma de las que contienen las expresiones de las que depende
        cuantas = []
        for var in range(len(cjto_variables)):
            c = []
            cuantas.append(Int("cuantas_" + str(i) + "_" + str(var))) # La variable i cuántas var contiene
            for exp in lista_expresiones[i]:
                c.append(cuantas_originales[exp][var])
                
            solver.add(Implies(activas[i], cuantas[var] == addsum(c)))
        
        cuantas_originales.append(cuantas)

    else: # Combinaciones iniciales
        cuantas = []
        for var in range(len(cjto_variables)):
            cuantas.append(Int("cuantas_" + str(i) + "_" + str(var))) # La variable i cuántas j contiene
            c = []
            for elem in lista_combinaciones[i]:
                if list(cjto_variables)[var] == elem:
                    c.append(1)
            solver.add(Implies(activas[i], cuantas[var] == addsum(c)))
        
        cuantas_originales.append(cuantas)

    # A la hora de reconstruir hay que quedarse con la expresión más general, que es la que contiene las demás y lleva la cuenta en total de todo

solver.add(addsum(cuenta_activas) <= max_intermedias)

# Debe existir una combinación de las expresiones tal que consigan bajar el grado del monomio a maxDeg
for m in range(num_monomios):
    selects = []  # Booleanos para indicar qué expresiones se usan para explicar el monomio m
    for exp in range(num_expresiones):
        b = Bool("select_" + str(m) + "_" + str(exp))
        selects.append(b)
        # Solo puedes seleccionar expresiones activas
        solver.add(Implies(b, activas[exp]))

    # Ahora forzamos que la suma ponderada de expresiones seleccionadas coincida con el monomio
    for var in range(len(cjto_variables)):
        suma = []
        for exp in range(num_expresiones):
            # If selected, cuenta esa cantidad de variable
            if num_variables_por_monomio[m][var] > 0:
                suma.append(If(selects[exp], cuantas_originales[exp][var], 0))
        solver.add(addsum(suma) == num_variables_por_monomio[m][var])

    # Finalmente, al menos una expresión debe ser usada para cubrir el monomio
    solver.add(addexists(selects))

# print(lista_expresiones)

# def reconstruir_expresiones(id, reconstrucciones):
#     if id < len(reconstrucciones): # Ya está calculado
#         return reconstrucciones[id]
#     else:
#         expresion = []
#         for e in lista_expresiones[id]:
#             expr = reconstruir_expresiones(e, reconstrucciones)
#             for elem in expr: expresion.append(elem)
#         return expresion

# # Reconstruir variables intermedias creadas
# reconstrucciones = []
# # ya_vistas = set()

# # Tienen que estar todas las combinaciones porque aunque generen la misma expresión luego se quedará con la que use menos variables
# for i in range(num_expresiones):
#     if i < len(combinaciones):
#         expr = list(lista_combinaciones[i])
#     else: 
#         expr = reconstruir_expresiones(i, reconstrucciones)

#     # expr_key = tuple(sorted(expr)) 

#     # # Para evitar repetidos
#     # if expr_key not in ya_vistas:
#     #     ya_vistas.add(expr_key)
#     reconstrucciones.append(expr)

# # grados = []
# # for p in range(num_polinomios):
#     # monomios = polinomios[p]["monomials"]
# for i in range(num_monomios):
#     deg = []

#     f = factores[i]
#     # Solo si la contiene y el keep está a true entonces el grado se modifica. 
#     # Puedo llevarlo separado por monomio para no tener que mirar si está contenido todo el rato????
#     for e in range(num_expresiones - 1, -1, -1):
#         if contains(f, reconstrucciones[e]):
#             deg.append(If(activas[e], len(reconstrucciones[e]) - 1, 0))

#             # Elimino los elementos de f porque ya han sido sustituidos
#             # for item in reconstrucciones[e]:
#             #     f.remove(item)

#     # grados.append(deg)
#     solver.add(grados_monomios[i] == degrees[i] - addsum(deg))

# if solver.check() == sat:
#     m = solver.model()

#     for i in range(len(activas)):
#         if is_true(m.eval(activas[i])):
#             combo = reconstrucciones[i]
#             nombre_variable = "*".join(combo) # Convierte la tupla ('x_1', 'x_2') a "x_1*x_2"
#             print(f"Variable intermedia seleccionada: {nombre_variable}")

# else: print("unsat")

# print(solver.assertions())
# file.write(solver.to_smt2())