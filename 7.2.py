nome_arquivo = input("digite o nome do arquivo: ")
with open(nome_arquivo) as arquivo:
    quantidade_linha= len(arquivo.readlines())
    print(quantidade_linha)