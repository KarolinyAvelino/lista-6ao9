from typing import List

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"O seu nome é {self.nome} e você tem {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__ (self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Salário: R${self.salario}")

pessoas: List[Pessoa] = []

pessoas.append(Pessoa("João", 35))
pessoas.append(Pessoa("Maria", 30))
pessoas.append(Funcionario("MarcosPaulo", 45, 1200))
pessoas.append(Funcionario("DanielHenrique", 25, 5500))

for p in pessoas:
    p.mostrar_dados()
    print("---------------------------------------------------")