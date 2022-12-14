
"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]


# estilo imperativo

def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)

print(*list(filter(starts_with_b, names)))


# estilo funcional
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")