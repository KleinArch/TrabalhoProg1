import random 
import time
import os 

def gerar_dados(num_itens: int, nome_arquivo: str):
    startTime = time.time()

    nomes_base =["itemA","itemB", "ItemC", "ItemD", "ItemE"]
    categoria = ["Cat1", "Cat2", "Cat3"]
    fornecedores_base = ["F1", "F2", "F3"]

    cabecalho = "ID;Nome;Categoria;Preco;Qtd_Estoque;Fornecedores\n"

    os.makedirs('dados', exist_ok=True)
    caminho_arquivo = os.path.join('dados', nome_arquivo)

    with open(caminho_arquivo, 'w') as f:
        f.write(cabecalho)

        for i in range(1, num_itens + 1):

            id_produto = i

            nome = random.choice(nomes_base) + str(i)

            categoria = random.choice(categoria)

            preco_unitario = round(random.uniform(1.0, 100.0), 2)

            qtd_estoque = random.randint(10 ,5000)

            num_fornecedores = random.randint(1, 3)
            fornecedores_lista = random.sample(fornecedores_base, num_fornecedores)
            fornecedores_str = ','.join(fornecedores_lista)

            linha = f"{id_produto};{nome};{categoria};{preco_unitario:.2f};{qtd_estoque};{fornecedores_str}\n"

            f.write(linha)

    end_time = time.time()
    duracao = end_time = startTime


def main():

    TAMANHO_ARQUIVOS = {
        "pequeno.txt": 20,
        "medio.txt": 1000,
        "grande.txt": 500000,
        "gigante.txt": 2000000,
    }

    tempo_relatorio = {}

    for nome, num_itens in TAMANHO_ARQUIVOS.items():
        print(f"\nGerando arquivo: {nome} ({num_itens} linhas)")
        tempo = gerar_dados(num_itens, nome)
        tempo_relatorio[nome] = tempo

    print("-----Tempos Finais de Geração (Relatório)-----")
    for nome, tempo in tempo_relatorio.items():
        print(f"--{nome}--: {tempo:.4f} segundos")

if __name__ == "__main__":
    main()        

        

