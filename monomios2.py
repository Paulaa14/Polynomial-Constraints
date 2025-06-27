#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mínimo número de factores con los que se puede reducir el grado de un monomio sin pasarme de grado en ningún factor
import argparse
import itertools
import json

# Una lista está contenida dentro de otra
def contains(variables, target):
    vars_copy = list(variables)  # Copia para no modificar la original
    for t in target:
        if t in vars_copy:
            vars_copy.remove(t) 
        else:
            return False
    return True

def min_factores_monomio(monomio, degree, maxDeg, vistos): # Monomio, grado actual del monomio y máximo grado permitido
    if degree < maxDeg: return monomio
    else:
        monomio = sorted(monomio)
        # Cojo agrupaciones del máximo grado posible, así se consigue el menor número de factores
        r = min(degree, maxDeg)
        posibilidades = []
        
        for combo in itertools.combinations(monomio, r):
            combo_sorted = tuple(sorted(combo))
            # print("combo " + str(combo_sorted))
            if combo_sorted not in vistos:
                vistos.add(combo_sorted)
                restante = list(monomio) # Copia

                count = 0
                while contains(restante, combo_sorted): # Quita todas las apariciones del factor
                    count += 1
                    for e in combo:
                        restante.remove(e)

                subsoluciones = min_factores_monomio(restante, degree - count * len(combo), maxDeg, vistos)

                l = [combo_sorted] + subsoluciones # Primero los factores

                posibilidades.append(l) # OK
                # for sub in subsoluciones:

        min_len = float('inf')
        min_elem = []
        for elem in posibilidades:
            if len(elem) < min_len:
                min_len = len(elem)
                min_elem = []
                min_elem.append(elem)
            elif len(elem) == min_len: # and not(elem) in min_elem: # Evitar repetidos
                min_elem.append(elem)
        
        return min_elem
    
def expand_factors(factors): # [x_1, x_1, x_2]
    expanded = []

    for f in factors:
        var = 'x_' + str(f["signal"])
        expanded.extend([var] * f["degree"])
    return expanded

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
num_monomios = 0

fact = set()
lista_conjuntos_monomios = []
lista_monomios = []
for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    lista_monomios.append(monomios)
    num_monomios += len(monomios)

    for m in monomios:
        factors = expand_factors(m["factors"])
        s = min_factores_monomio(factors, len(factors), maxDeg, set())

        print(s)
        mon = set()
        factorizacion = []

        for f in s:
            for elem in f:
                fact.add(elem)
                # mon.add(elem)
            factorizacion.append(f)
            mon = set()
        lista_conjuntos_monomios.append(factorizacion)

# fact contiene los factores comunes de todos los monomios
fact = list(fact)
fact.sort(key = len)
print(fact)

lista_conjuntos_monomios.sort(key=len) # Pongo los polinomios que tienen menos factorizaciones posibles primero
print(lista_conjuntos_monomios) # Cada monomio, qué factores necesita sí o sí, posibles factorizaciones

for factor in fact:
    for m in lista_monomios:
        break