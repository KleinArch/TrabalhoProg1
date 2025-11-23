import random
import time
import os

# ----------------------- ETAPA 1: GERAR ARQUIVOS ------------------------

def gerar_dados(num_itens: int, nome_arquivo: str):
    startTime = time.time() #começa a contar o timer

    nomes_base = ["itemA", "itemB", "ItemC", "ItemD", "ItemE"]
    categorias_base = ["Cat1", "Cat2", "Cat3"]
    fornecedores_base = ["F1", "F2", "F3"]

    cabecalho = "ID;Nome;Categoria;Preco;Qtd_Estoque;Fornecedores\n" # mostra como as linhas são formatadas

    os.makedirs('dados', exist_ok=True) # cria o diretório
    caminho_arquivo = os.path.join('dados', nome_arquivo)

    with open(caminho_arquivo, 'w') as f: # abre o diretorio e começa a edita-lo
        f.write(cabecalho)

        for i in range(1, num_itens + 1):

            id_produto = i
            nome = random.choice(nomes_base) + str(i)
            categoria = random.choice(categorias_base)
            preco_unitario = round(random.uniform(1.0, 100.0), 2)
            qtd_estoque = random.randint(10, 5000)

            num_fornecedores = random.randint(1, 3)
            fornecedores_lista = random.sample(fornecedores_base, num_fornecedores)
            fornecedores_str = ",".join(fornecedores_lista)

            linha = f"{id_produto};{nome};{categoria};{preco_unitario:.2f};{qtd_estoque};{fornecedores_str}\n"
            f.write(linha)

    end_time = time.time()
    duracao = end_time - startTime
    return duracao


# ----------------------- ETAPA 2: LEITURA COM CLASSES ------------------------

# Classe Produto — armazenará cada linha do arquivo
class Produto:
    def __init__(self, id_produto, nome, categoria, preco, qtd_estoque, fornecedores):
        self.id = int(id_produto)
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.qtd_estoque = int(qtd_estoque)
        self.fornecedores = fornecedores   # lista real!

    def __repr__(self):
        return f"Produto({self.id}, {self.nome}, {self.categoria})"


def ler_arquivo(nome_arquivo: str):
    start_time = time.time()

    caminho = os.path.join("dados", nome_arquivo)
    produtos = []

    with open(caminho, "r") as f:
        next(f)  # pular cabeçalho

        for linha in f:
            campos = linha.strip().split(";")
            fornecedores = campos[5].split(",")

            produto = Produto(
                id_produto=campos[0],
                nome=campos[1],
                categoria=campos[2],
                preco=campos[3],
                qtd_estoque=campos[4],
                fornecedores=fornecedores
            )

            produtos.append(produto)

    end_time = time.time()
    duracao = end_time - start_time

    return produtos, duracao


# ----------------------- MAIN ------------------------

def main():

    TAMANHO_ARQUIVOS = {
        "pequeno.txt": 20,
        "medio.txt": 1000,
        "grande.txt": 500000,
        "gigante.txt": 1000000,
    }

    tempo_geracao = {}
    tempo_leitura = {}

    for nome, num_itens in TAMANHO_ARQUIVOS.items():
        print(f"\nGerando arquivo: {nome} ({num_itens} linhas)")
        tempo = gerar_dados(num_itens, nome)
        tempo_geracao[nome] = tempo

        print(f"Lendo arquivo: {nome}")
        lista_produtos, tempo_ler = ler_arquivo(nome)
        tempo_leitura[nome] = tempo_ler

        # Exemplo: mostrar o 1º elemento (só para inspeção)
        print("Exemplo de produto lido:", lista_produtos[0])

    print("\n----- TEMPOS DE GERAÇÃO -----")
    for nome, tempo in tempo_geracao.items():
        print(f"{nome}: {tempo:.4f}s")

    print("\n----- TEMPOS DE LEITURA -----")
    for nome, tempo in tempo_leitura.items():
        print(f"{nome}: {tempo:.4f}s")


if __name__ == "__main__":
    main()
