class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"O seu nome é {self.nome} e você tem {self.idade} anos.")

class Cliente(Pessoa):
    def __init__ (self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco
    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Endereço: {self.endereco}")

c1 = Cliente("Livia de Souza", 40, "Mimoso do Sul-ES")
c1.mostrar_dados()