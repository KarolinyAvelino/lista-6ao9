nome_arquivo = input("digite o nome do arquivo: ")
with open(nome_arquivo) as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)