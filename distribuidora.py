import random
import string
import time
import os
'''print("____________________________\nBem Vindo ao DashBoard\n____________________________\n")
while True:
    print("Qual funão deseja acessar?\nSelecionar banco de dados(1)\nVisualizar banco de dados(2)\n\
          Criar bancos de dados(3)\nVisualizar resultados(4)")'''  
n = int(input("qual tamanho de aruivo deseja gerar?\n(1-pequeno)(2-médio)(3-grande)(4-gigante)\n"))
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
        with open("pequeno.txt", "w") as arquivo:
            arquivo.write('')
            arquivo.close()
        for i in range(20):
            with open("pequeno.txt", "r+") as arquivo:
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
        with open("medio.txt", "w") as arquivo:
            arquivo.write('')
            arquivo.close()
        for i in range(1000):
            with open("medio.txt", "r+") as arquivo:
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
        with open("grande.txt", "w") as arquivo:
            arquivo.write('')
            arquivo.close()
        for i in range(500000):
            with open("grande.txt", "r+") as arquivo:
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
        with open("gigante.txt", "w") as arquivo:
            arquivo.write('')
            arquivo.close()
        for i in range(1000000):
            with open("gigante.txt", "r+") as arquivo:
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