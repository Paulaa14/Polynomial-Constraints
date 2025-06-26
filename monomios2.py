#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Mínimo número de factores con los que se puede reducir el grado de un monomio sin pasarme de grado en ningún factor
import argparse
import itertools
import json


def min_factores_monomio(monomio, degree, maxDeg, mejor_len, path = []): # Monomio, grado actual del monomio y máximo grado permitido
    if degree < maxDeg: return [monomio]
    elif len(path) > mejor_len: return [monomio]
    else:
        monomio = sorted(monomio)
        # Cojo agrupaciones del máximo grado posible, así se consigue el menor número de factores
        vistos = set()
        r = min(degree, maxDeg)
        posibilidades = []

        for combo in itertools.combinations(monomio, r):
            combo_sorted = tuple(sorted(combo))
            if not(combo_sorted in vistos):
                vistos.add(combo_sorted)

                restante = list(monomio)
                for e in combo:
                    restante.remove(e)

                subsoluciones = min_factores_monomio(restante, degree - len(combo), maxDeg, min(mejor_len, len(path) + len(combo)), path)
                
                for sub in subsoluciones:
                    posibilidades.append([combo_sorted] + sub)

        if not posibilidades:
            return []
        
        min_len = float('inf')
        min_elem = []
        for elem in posibilidades:
            if len(elem) < min_len:
                min_len = len(elem)
                min_elem = []
                min_elem.append(elem)
            elif len(elem) == min_len and not(elem) in min_elem: # Evitar repetidos
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
for p in range(num_polinomios):
    monomios = polinomios[p]["monomials"]
    num_monomios += len(monomios)

    for m in monomios:
        factors = expand_factors(m["factors"])
        s = min_factores_monomio(factors, len(factors), maxDeg, float('inf'))

        for f in s:
            for elem in f:
                fact.add(elem)

print(fact)