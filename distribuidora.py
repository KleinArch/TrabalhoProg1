class Produto:
    def __init__(self, id_, nome, preco, quantidade):
        self.id = id_
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade

class Distribuidora:
    def __init__(self):
        self.produtos = []

    def carregar(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            next(f)
            for linha in f:
                partes = linha.strip().split(',')
                if len(partes) == 4:
                    id_, nome, preco, qtd = partes
                    produto = Produto(int(id_), nome, float(preco), int(qtd))
                    self.produtos.append(produto)