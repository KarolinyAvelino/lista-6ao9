class Veiculo:
    def __init__ (self, velocidade):
        self.velocidade = velocidade

    def acelerar(self, tempo):
        aceleracao = 10
        self.velocidade += aceleracao * tempo

    def frear(self, tempo):
        desaceleracao = 5
        self.velocidade -= desaceleracao * tempo

    def exibir_velocidade(self):
        print(f"A velocidade do veículo é de: {self.velocidade} Km/h")

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca

c1 = Carro(150, "Honda Civic")
c1.acelerar(15)
c1.exibir_velocidade()
c1.frear(5)
c1.exibir_velocidade()