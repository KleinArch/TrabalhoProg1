import random
import string
import time
import os

produtos = []

# ----------------------- ETAPA 2: LEITURA COM CLASSES ------------------------

# Classe Produto — armazenará cada linha do arquivo
class Produto:
    def __init__(self, id_produto, nome, categoria, preco, fornecedores):
        self.id = int(id_produto)
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
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

            fornecedores = str(fornecedor)

            produto = Produto(
                id_produto=id_produto,
                nome=nome,
                categoria=categoria,
                preco=preco,
                fornecedores=fornecedores
            )

            produtos.append(produto)

    return produtos



print("__________________________\nBem Vindo(a) ao DashBoard\n__________________________\n")
while True:
    print("Qual função deseja acessar?\n|Selecionar banco de dados(1)\n|Visualizar banco de dados(2)\n|Criar bancos de dados(3)\n|Visualizar resultados(4)\n|Sair(0)")
    resposta = int(input(":"))

    if resposta == 1:
        m = int(input("Qual banco deseja acessar?\n(1-pequeno 2-médio 3-grande 4-gigante)\n:"))

        if m == 1:
           produtos = ler_arquivo("pequeno.txt")
        elif m == 2:
           produtos = ler_arquivo("medio.txt")
        elif m == 3:
           produtos = ler_arquivo("grande.txt")
        elif m == 4:
           produtos = ler_arquivo("gigante.txt")

        a = int(input("Deseja adicionar uma linha(1), alterar uma linha(2) ou excluir uma linha(3)?\n:"))

        if a == 1:
            adicionar_produto(produtos)
        elif a == 2:
            alterar_linha(produtos)

    if resposta == 3:
        def geraArquivos():
            os.makedirs('dados', exist_ok=True)
            n = int(input("qual tamanho de arquivo deseja gerar?\n(1-pequeno 2-médio 3-grande 4-gigante)\n:"))
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
                saida = 0
                inteiro = random.randint(1,1000)
                decimal = random.randint(0,99)
                saida = float(f'{inteiro}.{decimal}')
                return saida
            def criaDados(n):
                listaFornecedores = []
                if n == 1:
                    with open("dados/pequeno.txt", "w") as arquivo:
                        arquivo.write('')
                        arquivo.close()
                    for i in range(20):
                        with open("dados/pequeno.txt", "r+") as arquivo:
                            id = i+1
                            nomeFornecedor = geraFornecedores()
                            listaFornecedores += [nomeFornecedor]
                            nomeProduto = letrasAleatorias(5)
                            idproduto = 1
                            while nomeProduto in arquivo:
                                nomeProduto = f'{nomeProduto}_{idproduto}'
                                idproduto += 1
                            precoProduto = precosAleatorios()
                            categoria = random.choice(categorias)
                            arquivo.write(f"{id}|{categoria}|{nomeProduto}_{idproduto}|{precoProduto}|{nomeFornecedor}\n")
                if n == 2:
                    with open("dados/medio.txt", "w") as arquivo:
                        arquivo.write('')
                        arquivo.close()
                    for i in range(1000):
                        with open("dados/medio.txt", "r+") as arquivo:
                            id = i+1
                            nomeFornecedor = geraFornecedores()
                            listaFornecedores += [nomeFornecedor]
                            nomeProduto = letrasAleatorias(5)
                            idproduto = 1
                            while nomeProduto in arquivo:
                                nomeProduto = f'{nomeProduto}_{idproduto}'
                                idproduto += 1
                            precoProduto = precosAleatorios()
                            categoria = random.choice(categorias)
                            arquivo.write(f"{id}|{categoria}|{nomeProduto}_{idproduto}|{precoProduto}|{nomeFornecedor}\n")
                elif n == 3:
                    with open("dados/grande.txt", "w") as arquivo:
                        arquivo.write('')
                        arquivo.close()
                    for i in range(4000):
                        with open("dados/grande.txt", "r+") as arquivo:
                            id = i+1
                            nomeFornecedor = geraFornecedores()
                            listaFornecedores += [nomeFornecedor]
                            nomeProduto = letrasAleatorias(5)
                            idproduto = 1
                            while nomeProduto in arquivo:
                                nomeProduto = f'{nomeProduto}_{idproduto}'
                                idproduto += 1
                            precoProduto = precosAleatorios() categoria = random.choice(categorias)
                            arquivo.write(f"{id}|{categoria}|{nomeProduto}_{idproduto}|{precoProduto}|{nomeFornecedor}\n")
                elif n == 4:
                    with open("dados/gigante.txt", "w") as arquivo:
                        arquivo.write('')
                        arquivo.close()
                    for i in range(20000):
                        with open("dados/gigante.txt", "r+") as arquivo:
                            id = i+1
                            nomeFornecedor = geraFornecedores()
                            listaFornecedores += [nomeFornecedor]
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
    #adicionar elif com as outras funções do programa
    else:
        break



#------------ETAPA 3: Manipulação de Dados e Visualização-------------------------


def adicionar_produto(produtos):
    print("\n--- Adicionar Novo Produto ---")

    id_produto = input("ID do produto: ")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    fornecedor = input("Fornecedor: ")

    novo = Produto(
        id_produto=id_produto,
        nome=nome,
        categoria=categoria,
        preco=preco,
        fornecedores=[fornecedor]
    )

    produtos.append(novo)

    print("\nProduto adicionado com sucesso!")
    print(novo)  # usa repr

def alterar_linha(produtos):
    print("\n---Alterando linha---")
    n = int(input("Qual linha deseja alterar?\n:"))

    id_produto = input("ID do produto: ")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    fornecedor = input("Fornecedor: ")

    novo = Produto(
        id_produto=id_produto,
        nome=nome,
        categoria=categoria,
        preco=preco,
        fornecedores=[fornecedor]
    )

    produtos[n] = novo

    print("\nProduto adicionado com sucesso!")
    print(novo)  # usa repr

