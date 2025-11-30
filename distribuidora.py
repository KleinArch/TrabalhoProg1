import random
import string
import time
import os

print("__________________________\nBem Vindo(a) ao DashBoard\n__________________________\n")

#-------------------------------------------------------------------------------------------
#Etapa 2 - Classes e Funções
#-------------------------------------------------------------------------------------------

class Produto:
    def __init__(self, id_produto, nome, categoria, preco, fornecedores, quantidades):
        self.id = int(id_produto)
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.fornecedores = fornecedores   # lista real
        self.quantidades = quantidades

    def __repr__(self):
        return f"Produto({self.id}, {self.nome}, {self.categoria}, {self.preco}, {self.fornecedores}, {self.quantidades})"

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
            # ID | CATEGORIA | NOME | PRECO | FORNECEDOR | QUANTIDADES

            id_produto = campos[0]
            categoria = campos[1]
            nome = campos[2]
            preco = campos[3]
            fornecedor = campos[4]
            quantidades = campos[5]

            fornecedores = str(fornecedor)

            produto = Produto(
                id_produto=id_produto,
                nome=nome,
                categoria=categoria,
                preco=preco,
                fornecedores=fornecedores,
                quantidades=quantidades
            )

            produtos.append(produto)

    return produtos


#Função Adicionar Produto( ### Etapa 3)

def adicionar_linha(produtos):
    print("\n--- Adicionar Novo Produto ---")

    id_produto = len(produtos)+1
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    fornecedor = input("Fornecedor: ")
    quantidades = list(map(int,input("Quantidade(min max): ").split()))

    novo = Produto(
        id_produto=id_produto,
        nome=nome,
        categoria=categoria,
        preco=preco,
        fornecedores=str(fornecedor),
        quantidades=quantidades
    )

    produtos.append(novo)

    print("\nLinha adicionada com sucesso!")
    print(novo)  # usa repr

#Função Alterar_linha ( ### Etapa 3)
def alterar_linha(produtos):
    print("\n---Alterando linha---")

    n = int(input("Qual linha deseja alterar?\n:"))
    id_produto = n
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    fornecedor = input("Fornecedor: ")
    quantidades = list(map(int,input("Quantidade(min max): ").split()))

    novo = Produto(
        id_produto=id_produto,
        nome=nome,
        categoria=categoria,
        preco=preco,
        fornecedores=fornecedor,
        quantidades=quantidades
    )

    produtos[n-1] = novo

#----------------------------------------------
# Variaveis Globais
# ---------------------------------------------

produtos = []
arquivo_atual = None

#----------------------------------------------
#Menu principal
#----------------------------------------------

while True:
    print("Qual função deseja acessar?\n"
          "|Selecionar banco de dados(1)\n"
          "|Visualizar banco de dados(2)\n"
          "|Criar bancos de dados(3)\n"
          "|Adicionar nova linha(4)\n"
          "|Alterar linha(5)\n"
          "|Remover linha(6)\n"
          "|Saída de Dados(7)\n"
          "|Sair(0)")
    
    resposta = int(input(":"))

    #Opção 1 - Selecionar Banco
    
    if resposta == 1:
        print("\nSelecione o arquivo:")
        print("1 - pequeno.txt")
        print("2 - medio.txt")
        print("3 - grande.txt")
        print("4 - gigante.txt")

        escolha = int(input(":"))

        if escolha == 1:
            arquivo_atual = "pequeno.txt"
        elif escolha == 2:
            arquivo_atual = "medio.txt"  
        elif escolha == 3:
            arquivo_atual = "grande.txt"
        elif escolha == 4:
            arquivo_atual = "gigante.txt"
        else:
            print("Opção Inválida.\n")
            continue

        produtos = ler_arquivo(arquivo_atual)
        print(f"Arquivo {arquivo_atual} carregado. {len(produtos)} produtos lidos")

        #Opção 2 - Vizualizar Produtos
    elif resposta == 2:
        if not produtos:
            print("\nNenhum banco carregado! Use a opção 1 primeiro.\n")
        else:
            print("\n ID | NOME | CATEGORIA | PRECO | FORNECEDOR | QUANTIDADES")
            print("\n--- Produtos carregados ---")
            for p in produtos:
                print(p)

#-------------------------------------------------------------------------------------------
#Etapa 1 - Classes e Funções
#-------------------------------------------------------------------------------------------

        #Opção 3 - Gerar arquivos
    elif resposta == 3:
        def geraArquivos():
            os.makedirs('dados', exist_ok=True)
            n = int(input("qual tamanho de arquivo deseja gerar?\n(1-pequeno 2-médio 3-grande 4-gigante)\n:"))
            print("Gerando dados...")
            categorias = ["Alimento", "Bebida", 'Utensílio']
            def geraQuatidades():
                lista = [random.randint(1,20),random.randint(25,80)]
                return lista
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
                categorias = ["Alimento", "Bebida", 'Utensílio']
                if n == 1:
                    nome = "pequeno.txt"
                    quantidade = 20
                elif n == 2:
                    nome = "medio.txt"
                    quantidade = 1000
                elif n == 3:
                    nome = "grande.txt"
                    quantidade = 40000
                elif n == 4:
                    nome = "gigante.txt"
                    quantidade = 140000
                else:
                    return

                with open(f"dados/{nome}", "w") as arquivo:
                    arquivo.write("")

                for i in range(quantidade):
                    with open(f"dados/{nome}", "a") as arquivo:
                        id = i + 1
                        nomeFornecedor = geraFornecedores()
                        nomeProduto = letrasAleatorias(5) + f"{id}"
                        precoProduto = precosAleatorios()
                        categoria = random.choice(categorias)
                        quantidades = geraQuatidades()
                        arquivo.write(f"{id}|{categoria}|{nomeProduto}|{precoProduto}|{nomeFornecedor}|{quantidades}\n")

            star = time.time()
            criaDados(n)
            end = time.time()
            return f"A operação durou {end - star:.3f}s"

        print("\n")
        print(geraArquivos())
        print("\n...de volta ao menu princilpal")

    # OPÇÃO 4 — ADICIONAR NOVA LINHA
    elif resposta == 4:
        if not produtos:
            print("\nNenhum banco carregado! Use a opção 1 primeiro.\n")
        else:
            adicionar_linha(produtos)   

    # OPÇÃO 5 — ALTERAR LINHA
    elif resposta == 5:
        if not produtos:
            print("\nNenhum banco carregado! Use a opção 1 primeiro.\n")
        else:
            alterar_linha(produtos) 

# OPÇÃO 6 — REMOVER LINHA
    elif resposta == 6:
        if not produtos:
            print("\nNenhum banco carregado! Use a opção 1 primeiro.\n")
        else:
            remover = int(input("Qual linha deseja remover?:"))
            produtos.pop(remover-1)

    #Opção 7 - Resultados
    elif resposta == 7:
        with open("dados/resultados.txt", "w") as arquivo:
            arquivo.write("")
        with open("dados/resultados.txt", "a") as arquivo:
            arquivo.write("ID | NOME | CATEGORIA | PRECO | FORNECEDOR | QUANTIDADES\n")
            for p in produtos:
                arquivo.write(f'{p}\n')

    #FIM
    else:
        break                

