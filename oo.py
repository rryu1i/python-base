from decimal import Decimal


class Produto:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = Decimal(valor)

opt_1 = Produto(nome="Maca", valor=4.5)
opt_2 = Produto(nome="Melancia", valor=6.3)

produtos = {
    "1": opt_1,
    "2": opt_2
}


def interface():
    print("Ola cliente, boas vindas a quitanda!")
    print("Estes sao os produtos disponivels:")
    for key, value in produtos.items():
        print(
            f"{key} -> {value.nome} - R$ {value.valor:.2f}"
        )


class Item:
    def __init__(self, produto, quantidade) -> None:
        self.produto = produto
        self.quantidade = quantidade


class Compra:
    def __init__(self, cliente, items=None) -> None:
        self.cliente = cliente
        self.items = items or []

    @property
    def total(self):
        total = sum(
            [item.produto.valor * item.quantidade for item in self.items]
        )
        return Decimal(total)

    def add_item(self, cod_produto, quantidade):
        self.items.append(Item(produtos[cod_produto], quantidade))



def main():
    interface()
    nome_cliente = input("Qual seu nome?")
    compra = Compra(nome_cliente)
    while True:
        cod_produto = input("Cod produto ou enter para sair").strip()
        if not cod_produto:
            break
        if cod_produto not in produtos:
            print("codigo invalido")
            continue
        quantidade = int(input("qts unidades").strip())
        compra.add_item(cod_produto, quantidade)
    print(f"ola {nome_cliente}")
    print(f"no seu carrinho ha {len(compra.items)} itens")
    print(f"o total da compra e {compra.total}")



main()
