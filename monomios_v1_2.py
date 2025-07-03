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
max_intermedias = 4

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

for nivel in range(num_niveles):
    variables_nivel = []
    for variable in range(num_variables_por_nivel):
        variables_nivel.append(Bool("x_" + str(nivel) + "_" + str(variable))) # Está activa la variable o no

    variables_intermedias.append(variables_nivel)

# De momento, cada nivel se forma con variables del nivel inmediatamente anterior y factores iniciales
dependencias = []
for nivel in range(num_niveles):
    deps_nivel = []
    for variable in range(num_variables_por_nivel):
        dependencias_variable = []
        cumple_grado = []
        cumple_var = []

        if nivel > 0:
            # La variable de nivel utiliza o no la variable del nivel anterior
            for variable_nivel_anterior in range(num_variables_por_nivel):
                dependencias_variable.append(Bool("depv_" + str(nivel) + "_" + str(variable) + "_" + str(variable_nivel_anterior))) 

                # Solo se puede utilizar si var está activa
                solver.add(Implies(dependencias_variable[variable_nivel_anterior], variables_intermedias[nivel - 1][variable_nivel_anterior]))

                # Si se utiliza esta variable de otro nivel, su grado es 1, sino 0
                cumple_grado.append(If(dependencias_variable[variable_nivel_anterior], 1, 0))

        # La variable elem de nivel utiliza o no el factor fact
        for factor in range(num_combinaciones):
            depf = Bool("depf_" + str(nivel) + "_" + str(variable) + "_" + str(factor))
            dependencias_variable.append(depf)

            # if nivel == 0 and variable == 0 and factor == num_combinaciones - 1:
            #     solver.assert_exprs(depf)
            # elif nivel == 0 and variable == 1 and factor == 2:
            #     solver.assert_exprs(depf)

            # Si se utiliza, su grado es el del factor ya que se va a sustituir
            cumple_grado.append(If(depf, len(lista_combinaciones[factor]), 0))

        # La suma del grado de todo lo que se utiliza para formar la variable debe ser menor o igual que el grado máximo
        solver.add(addsum(cumple_grado) <= maxDeg) # Creo que OK porque no superan el grado

        # Eliminar variables que están formadas por una única variable intermedia
        solver.add(Or(addsum(dependencias_variable) == 0, addsum(dependencias_variable) > 1))

        deps_nivel.append(dependencias_variable)

    dependencias.append(deps_nivel)

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

# Los monomios resultantes cumplen todos 0 <= grado <= maxDeg
deps_monomios = []
for mon in range(num_monomios):
    deps_mon = []
    cumple_grado = []
    de_cuantas_depende = []

    if num_niveles > 0:
        for variable in range(num_variables_por_nivel):
            deps_mon.append(Bool("depmv_" + str(mon) + "_" + str(variable)))

            # Solo se puede utilizar si var está activa
            solver.add(Implies(deps_mon[variable], variables_intermedias[num_niveles - 1][variable]))

            grado_expresion = []
            for variable_original in range(len(cjto_variables)):
                grado_expresion.append(If(deps_mon[variable], cuantas_variables[num_niveles - 1][variable][variable_original], 0))

            cumple_grado.append(If(deps_mon[variable], addsum(grado_expresion), 0))
            de_cuantas_depende.append(If(deps_mon[variable], 1, 0)) # Aporta grado 1

    for factor in range(num_combinaciones):
        elem = Bool("depmf" + str(mon) + "_" + str(factor))
        deps_mon.append(elem)
        de_cuantas_depende.append(If(elem, len(lista_combinaciones[factor]), 0)) # Aporta su grado

    deps_monomios.append(deps_mon)

    # expr_grado = len(lista_monomios[mon]) - addsum(cumple_grado) + addsum(de_cuantas_depende)

    # solver.add(expr_grado <= maxDeg)
    # solver.add(expr_grado >= 0)

    # restricciones_grado_expr.append(expr_grado)

    # CAMBIAR: LONGITUD INICIAL - SUMA DE LAS LONGITUDES DE LAS EXPRESIONES DE LAS QUE DEPENDE + NUMERO DE EXPRESIONES DE LAS QUE ESTÁ FORMADA
    solver.add(len(lista_monomios[mon]) - addsum(cumple_grado) + addsum(de_cuantas_depende) <= maxDeg)
    solver.add(len(lista_monomios[mon]) - addsum(cumple_grado) + addsum(de_cuantas_depende) >= 0)

# Cuento que se consigan todas las variables que tenía originalmente el monomio
for mon in range(num_monomios):
    for var in range(len(cjto_variables)):
        conteo_var = []
        if num_niveles > 0:
            for elem in range(num_variables_por_nivel):
                conteo_var.append(If(deps_monomios[mon][elem], cuantas_variables[num_niveles - 1][elem][var], 0))
        
            for fact in range(num_combinaciones):
                conteo_var.append(If(deps_monomios[mon][num_variables_por_nivel + fact], num_variables_por_factor[fact][var], 0))

        else:
            for fact in range(num_combinaciones):
                conteo_var.append(If(deps_monomios[mon][fact], num_variables_por_factor[fact][var], 0))

        solver.add(addsum(conteo_var) == num_variables_por_monomio[mon][var])

# Tiene que estar activa y existir una del nivel siguiente que la utilice junto con otra
cuentan = []
suma_cuentan = []
for nivel in range(num_niveles):
    for elem in range(num_variables_por_nivel):
        c = Bool("cuenta_" + str(nivel) + "_" + str(elem))
        suma_cuentan.append(If(c, 1, 0))
        cuentan.append(c)
        activas_sig_nivel = []
        if nivel < num_niveles - 1:
            # Hay alguna variable del siguiente nivel que tiene otra dependencia con un elemento de mi nivel que no es el que estoy mirando
            for aux in range(num_variables_por_nivel):
                auxiliar = []
                for var in range(num_variables_por_nivel):
                    if var != elem:
                        auxiliar.append(If(dependencias[nivel + 1][aux][var], 1, 0))

                for fact in range(num_combinaciones):
                    auxiliar.append(If(dependencias[nivel + 1][aux][fact + num_variables_por_nivel], 1, 0))

                # Tiene activas tanto elem como aux y tener dependencia aux con elem
                activas_sig_nivel.append(If(And(addsum(auxiliar) > 0, dependencias[nivel + 1][aux][elem], variables_intermedias[nivel + 1][aux]), 1, 0))
            
            # cuentan.append(If(And(variables_intermedias[nivel][elem], addsum(activas_sig_nivel) > 0), 1, 0))
            solver.add(Implies(And(variables_intermedias[nivel][elem], addsum(activas_sig_nivel) > 0), c))
            solver.add(Implies(c, And(variables_intermedias[nivel][elem], addsum(activas_sig_nivel) > 0)))
        
        else:
            # En el último nivel si está activa cuenta si la utiliza un monomio
            for mon in range(num_monomios):
                # for var in range(num_variables_por_nivel):
                # activas_sig_nivel.append(If(deps_monomios[mon][elem], 1, 0))
                # cuentan.append(If(And(variables_intermedias[nivel][elem], deps_monomios[mon][elem]), 1, 0)) 
                solver.add(Implies(And(variables_intermedias[nivel][elem], deps_monomios[mon][elem]), c))           
                solver.add(Implies(c, And(variables_intermedias[nivel][elem], deps_monomios[mon][elem])))           

solver.add(addsum(suma_cuentan) <= max_intermedias)

# file.write(solver.to_smt2())

if solver.check() == sat:
    m = solver.model()

    print("\n=== Variables intermedias activas y sus dependencias ===\n")
    for nivel in range(num_niveles):
        for elem in range(num_variables_por_nivel):
            var_activa = variables_intermedias[nivel][elem]
            if is_true(m.eval(var_activa)):
                print(f"Nivel {nivel}, Variable {elem}:")
                deps = dependencias[nivel][elem]
                usados = []

                # Dependencias con variables anteriores
                if nivel > 0:
                    for var_prev in range(num_variables_por_nivel):
                        if is_true(m.eval(deps[var_prev])):
                            usados.append(f"VI(n{nivel-1},v{var_prev})")

                # Dependencias con factores base
                offset = 0 if nivel == 0 else num_variables_por_nivel
                for fact in range(num_combinaciones):
                    dep_idx = offset + fact
                    if is_true(m.eval(deps[dep_idx])):
                        usados.append("*".join(lista_combinaciones[fact]))

                print("  → Compuesta por:", ", ".join(usados))

    print("\n=== Monomios finales y qué usan ===\n")
    for mon in range(num_monomios):
        usados = []
        deps = deps_monomios[mon]

        # Variables intermedias del último nivel
        for var in range(num_variables_por_nivel):
            if is_true(m.eval(deps[var])):
                usados.append(f"VI(n{num_niveles - 1},v{var})")

        # Factores base
        for fact in range(num_combinaciones):
            idx = num_variables_por_nivel + fact
            if is_true(m.eval(deps[idx])):
                usados.append("*".join(lista_combinaciones[fact]))

        print(f"Monomio {mon} usa: {', '.join(usados) if usados else 'Ninguna variable/intermedia usada'}")

    print("\n=== Valores del array 'cuentan' con sus variables ===\n")
    idx = 0
    for nivel in range(num_niveles):
        for elem in range(num_variables_por_nivel):
            val = m.eval(cuentan[idx], model_completion=True)
            print(f"cuentan[{idx}] (Nivel {nivel}, Variable {elem}) = {val}")
            idx += 1


    print("\n=== Conteo de variables en intermedias ===\n")
    for nivel in range(num_niveles):
        for elem in range(num_variables_por_nivel):
            if is_true(m.eval(variables_intermedias[nivel][elem])):
                print(f"VI(n{nivel},v{elem}): {[m.eval(cuantas_variables[nivel][elem][i]) for i in range(len(cjto_variables))]}")

    print("\n=== Conteo de variables en monomios ===\n")
    for mon in range(num_monomios):
        counts = []
        for i in range(len(cjto_variables)):
            sum_vi = addsum([
                If(deps_monomios[mon][vi], cuantas_variables[num_niveles - 1][vi][i], 0)
                for vi in range(num_variables_por_nivel)
            ])
            sum_fact = addsum([
                If(deps_monomios[mon][num_variables_por_nivel + f], num_variables_por_factor[f][i], 0)
                for f in range(num_combinaciones)
            ])
            counts.append(m.eval(sum_vi + sum_fact))
        print(f"Monomio {mon}: {counts}")

    for mon, deps in enumerate(deps_monomios):
        grado_real = 0
        print(f"Monomio {mon}:")

        for dep in deps:
            if m.eval(dep, model_completion=True):
                nombre = str(dep)
                if "depmv" in nombre:
                    idx = int(nombre.split("_")[2])
                    grado = sum([m.eval(cuantas_variables[num_niveles - 1][idx][v], model_completion=True).as_long() for v in range(len(cjto_variables))])
                    grado_real += grado
                    print(f"  Usa variable intermedia {idx} con grado {grado}")
                elif "depmf" in nombre:
                    idx = int(nombre.replace("depmf" + str(mon) + "_", ""))
                    grado = len(lista_combinaciones[int(idx)])
                    grado_real += grado
                    print(f"  Usa combinación {idx} con grado {grado}")

    print(f"  Grado total reconstruido: {grado_real}\n")

else:
    print("UNSAT: No se encontró solución.")

# file.write(str(solver.assertions()))

with open("debug_constraints.smt2", "w") as out:
    out.write(solver.to_smt2())