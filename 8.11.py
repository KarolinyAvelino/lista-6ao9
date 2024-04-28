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

    def aumentar_salario(self, aumento_percentual):
        aumento = self.salario * (aumento_percentual / 100)
        self.salario += aumento

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Salário: R${self.salario}")

f1 = Funcionario("Josiane", 50, 30000)
f1.aumentar_salario(10)  
f1.mostrar_dados()