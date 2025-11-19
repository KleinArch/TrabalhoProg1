class empresa:
    def __init__(self,nome):
        self.nome = nome
lista = []
with open("ex.txt", "r") as arquivo:
    for i in range(2):
        empresas = arquivo.readline()
        lista.append(empresas.split())
print(lista)

K = empresa('Sadia')
    