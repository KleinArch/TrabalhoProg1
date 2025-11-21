import random
import string
'''print("____________________________\nBem Vindo ao DashBoard\n____________________________\n")
while True:
    print("Qual funão deseja acessar?\nSelecionar banco de dados(1)\nVisualizar banco de dados(2)\n\
          Criar bancos de dados(3)\nVisualizar resultados(4)")'''

def letrasAleatorias(n):
    linha = ''
    for i in range(n):
        letra = random.choice(string.ascii_letters)
        linha += letra.upper()
    return linha
def precosAleatorios():
    saida = 0
    inteiro = random.randint(1,1000)
    decimal = random.randint(0,99)
    saida = float(f'{inteiro}.{decimal}')
    return saida
def funcPequena():
    with open("ex.txt", "w") as arquivo:
        arquivo.write('')
    for i in range(20):
        with open("ex.txt", "a") as arquivo:
            arquivo.write(f"{letrasAleatorias(5)},{precosAleatorios()}")