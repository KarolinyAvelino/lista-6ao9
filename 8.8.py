class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"O seu nome é {self.nome} e você tem {self.idade} anos.")

class Aluno(Pessoa):
    def __init__ (self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Matrícula: {self.matricula}")

a1 = Aluno("Karol", 18, "20211imi037")
a1.mostrar_dados()