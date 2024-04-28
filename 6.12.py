numeros_primos = [2, 3, 5, 7]
numeros_pares = [2, 4, 6, 8]

elementos_comuns = lambda numeros_primos, numeros_pares: list(filter(lambda x: x in numeros_pares, numeros_primos))
print(elementos_comuns(numeros_primos, numeros_pares))