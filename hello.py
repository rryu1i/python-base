#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument '--lang'

Ou o usuario tera que digitar.

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.0"  # Dunder version
__author__ = "Roger Ryuichi"
__license__ = "Unlicense"

import os
import sys


arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")  # retorna lista com key na pos 0 e value na pos 1
    key = key.lstrip("-").strip()  # lstrip pega todos os - do lado esquerda e remove
    value = value.strip()
    if key not in arguments:  
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")  # snake case
    # TODO: Usar repeticao
    if current_language is None:
        current_language = input(
            "Choose a language:"
        )

current_language = current_language[:5]
      
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

# O(1) - Constante - "IN"
print(msg[current_language] * int(arguments["count"]))