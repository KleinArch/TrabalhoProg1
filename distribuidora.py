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
            n = int(input("Qual tamanho de arquivo que deseja gerar?\n(1-pequeno 2-médio 3-grande 4-gigante)\n:"))
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
                            precoProduto = precosAleatorios()
                            categoria = random.choice(categorias)
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
