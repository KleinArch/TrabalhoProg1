# ----------------------- ETAPA 1: GERAR ARQUIVOS ------------------------

import random
import string
import time
import os

print("__________________________\nBem Vindo(a) ao DashBoard\n__________________________\n")

while True:
    print("Qual função deseja acessar?\n|Selecionar banco de dados(1)\n|Visualizar banco de dados(2)\n|Criar bancos de dados(3)\n|Visualizar resultados(4)\n|Sair(0)")
    resposta = int(input(":"))

    if resposta == 3:
        def geraArquivos():
            os.makedirs('dados', exist_ok=True)
            n = int(input("qual tamanho de aruivo deseja gerar?\n(1-pequeno 2-médio 3-grande 4-gigante)\n:"))
            print("Gerando dados...")

            categorias = ["Alimento", "Bebida", 'Utensílio']

            def letrasAleatorias(n):
                linha = ''
                for i in range(n):
                    letra = random.choice(string.ascii_letters).upper()
                    linha += letra
                return linha

            def geraFornecedores():
                dig1 = random.randint(0,9)
                dig2 = random.randint(0,9)
                dig3 = random.randint(0,9)
                dig4 = random.randint(0,9)
                letra1 = random.choice(string.ascii_letters).upper()
                letra2 = random.choice(string.ascii_letters).upper()
                return f'{letra1}{letra2}{dig1}{dig2}{dig3}{dig4}'

            def precosAleatorios():
                inteiro = random.randint(1,1000)
                decimal = random.randint(0,99)
                return float(f'{inteiro}.{decimal}')

            def criaDados(n):
                if n == 1:
                    nome = "dados/pequeno.txt"
                    quantidade = 20
                elif n == 2:
                    nome = "dados/medio.txt"
                    quantidade = 1000
                elif n == 3:
                    nome = "dados/grande.txt"
                    quantidade = 4000
                elif n == 4:
                    nome = "dados/gigante.txt"
                    quantidade = 20000

                with open(nome, "w") as arquivo:
                    arquivo.write('')

                for i in range(quantidade):
                    with open(nome, "r+") as arquivo:
                        id = i+1
                        nomeFornecedor = geraFornecedores()
                        nomeProduto = letrasAleatorias(5)
                        idproduto = 1

                        while nomeProduto in arquivo:
                            nomeProduto = f'{nomeProduto}_{idproduto}'
                            idproduto += 1

                        precoProduto = precosAleatorios()
                        categoria = random.choice(categorias)

                        arquivo.write(f"{id}|{categoria}|{nomeProduto}_{idproduto}|{precoProduto}|{nomeFornecedor}\n")

            startTime = time.time()
            criaDados(n)
            endTime = time.time()
            duracao = endTime - startTime

            return f'a operação durou:{duracao:.3f}s'

        print("\n")
        print(geraArquivos())
        print("\n...voltando ao menu inicial...\n\nBem vindo(a) de volta!\n")

    else:
        break



# ----------------------- ETAPA 2: LEITURA COM CLASSES ------------------------

# Classe Produto — armazenará cada linha do arquivo
class Produto:
    def __init__(self, id_produto, nome, categoria, preco, qtd_estoque, fornecedores):
        self.id = int(id_produto)
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.qtd_estoque = int(qtd_estoque)
        self.fornecedores = fornecedores   # lista real

    def __repr__(self):
        return f"Produto({self.id}, {self.nome}, {self.categoria})"

def ler_arquivo(nome_arquivo: str):

    caminho = os.path.join("dados", nome_arquivo)
    produtos = []

    with open(caminho, "r") as f:
        for linha in f:
            linha = linha.strip()

            if not linha:
                continue  # ignora linhas vazias

            campos = linha.split("|")

            # Formato gerado:
            # ID | CATEGORIA | NOME | PRECO | FORNECEDOR

            id_produto = campos[0]
            categoria = campos[1]
            nome = campos[2]
            preco = campos[3]
            fornecedor = campos[4]

            # Transformando em lista (mesmo tendo só 1 fornecedor)
            fornecedores = [fornecedor]

            # A etapa 1 NÃO tem estoque → definir padrão
            qtd_estoque = 0

            produto = Produto(
                id_produto=id_produto,
                nome=nome,
                categoria=categoria,
                preco=preco,
                qtd_estoque=qtd_estoque,
                fornecedores=fornecedores
            )

            produtos.append(produto)

    return produtos
