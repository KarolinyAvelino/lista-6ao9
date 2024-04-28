import os
nome_arquivo = str(input("Digite o nome do arquivo: "))
i_ponto= len(nome_arquivo) -4
novo_nome = nome_arquivo[:i_ponto]+ "_renomeado" + nome_arquivo[i_ponto:]
os.rename(nome_arquivo , nome_arquivo)