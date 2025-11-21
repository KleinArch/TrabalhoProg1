import random
import time
import os

##ETAPA 2:
class Produto:
    def __init__(self, id_produto: int, nome: str, categoria: str,
                 preco_unitario: float, qtd_estoque: int, fornecedores: list):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.qtd_estoque = qtd_estoque
        self.fornecedores = fornecedores

    def __str__(self):
        return (f"ID: {self.id_produto:<4} | Nome: {self.nome:<20} | Categoria: {self.categoria:<10} | "
                f"Preço: R${self.preco_unitario:>7.2f} | Estoque: {self.qtd_estoque:>5} | "
                f"Fornecedores: {', '.join(self.fornecedores)}")

    def to_file_line(self):
        fornecedores_str = ';'.join(self.fornecedores)
        return (f"{self.id_produto}||{self.nome}||{self.categoria}||"
                f"{self.preco_unitario:.2f}||{self.qtd_estoque}||{fornecedores_str}\n")
    


def ler_dados_do_arquivo(nome_arquivo: str):
    start_time = time.time()

    produtos = []
    caminho_arquivo = os.path.join('data', nome_arquivo)

    print(f"-> Lendo dados do arquivo: {caminho_arquivo}...")

    try:
        with open(caminho_arquivo, 'r') as f:
            next(f)

            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue

                partes = linha.split('||')

                if len(partes) != 6:
                    print(f"AVISO: Linha ignorada devido a formato incorreto: {linha}")
                    continue

                try:
                    id_produto = int(partes[0])
                    nome = partes[1]
                    categoria = partes[2]
                    preco_unitario = float(partes[3])
                    qtd_estoque = int(partes[4])
                    fornecedores = partes[5].split(';') if partes[5] else []

                    produto = Produto(id_produto, nome, categoria, preco_unitario, qtd_estoque, fornecedores)
                    produtos.append(produto)

                except ValueError as e:
                    print(f"ERRO DE CONVERSÃO: Não foi possível processar a linha: {linha}. Erro: {e}")

    except FileNotFoundError:
        print(f"ERRO: Arquivo '{caminho_arquivo}' não encontrado.")
        return [], 0.0

    end_time = time.time()
    tempo_computacional = end_time - start_time
    print(f"   Concluído. Total de {len(produtos)} produtos carregados. Tempo de leitura: {tempo_computacional:.4f} segundos.")
    return produtos, tempo_computacional

if __name__ == "__main__":
    main()