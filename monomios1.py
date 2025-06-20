#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Primero como un problema SAT, puedo resolverlo con 2 variables intermedias? 3? Teniendo como grado máximo permitido 2 por ejemplo.
# Aparecen muchas simetrías de soluciones que solamente se diferencian en el renombrado de las variables. Se pueden controlar numerando u ordenando.

import json

# Primera aproximación: 

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("filein", help=".json file including the tree structure",
                    type=str)
parser.add_argument("fileout", help= "Output file with the new expressions")


args=parser.parse_args()

# Opening JSON file
f = open(args.filein)
data = json.load(f)

file = open(args.fileout, "w")