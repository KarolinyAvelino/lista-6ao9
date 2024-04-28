nome_arquivo = input("digite o nome do arquivo: ")
with open(nome_arquivo) as arquivo:
    linhas = arquivo.readlines()
    with open("texto_invertido.txt", "w") as arquivo_invertido:
        for linha in linhas:
            arquivo_invertido.write(linha.strip()[::-1] + "\n")

    