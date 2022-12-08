#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

1 x 1 = 1
2 x 1 = 2
3 x 1 = 3
...
##########
---Tabuada do 2---
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
##########

"""
__version__ = "0.1.1"
__author__ = "Roger"


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))  # range e nao inclusivo

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        operacao = f"{n1} x {n2} = {resultado}"
        print("{:^18}".format(operacao))
    print("#" * 18)
