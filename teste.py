lista = []
with open("ex.txt", "r") as arquivo:
    for i in range(2):
        empresas = arquivo.readline()
        lista.append(empresas.split())
print(lista)
    