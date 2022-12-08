#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"  # Dunder version
__author__ = "Roger Ryuichi"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US.utf8")[:5]  # snake case
      
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"


print(msg)