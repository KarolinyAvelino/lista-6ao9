def filtrar_elementos(lista, funcao):
    return list(filter(funcao, lista))

def eh_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = filtrar_elementos(numeros, eh_par)
print(numeros_pares) 