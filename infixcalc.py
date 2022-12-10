#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

"""
__version__ = "0.1.0"

import os
import sys


arguments = sys.argv[1:]

op, a, b = arguments
a = int(a)
b = int(b)

if op == "sum":
    print(a + b)
elif op == "sub":
    print(a - b)
elif op == "mul":
    print(a * b)
elif op == "div":
    print(a / b)



