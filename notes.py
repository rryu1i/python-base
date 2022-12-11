#!/user/bin/env python3
"""Bloco de Notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

# notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys


cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid Usage")
    print("you must specify a subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")


if arguments[0] == "read":
    for line_ in open(filepath):
        title, tag, text = line_.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()



if arguments[0] == "new":
    titulo = arguments[1]  # TODO: Tratar exception
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv tab separated values
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")