email_templ = """
Ola, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto e otimo para resolver
%(texto)s

Clique agora em link %(link)s

Apenas %(quantidade)d disponiveis!

Preco promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_templ
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )

