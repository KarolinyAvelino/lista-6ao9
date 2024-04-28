class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo, taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def calcular_rendimento(self):
        rendimento = self.saldo * (self.taxa_juros / 100) * 12
        self.saldo += rendimento
        print(f"Rendimento mensal: R${self.saldo:.2f}")

cp1 = ContaPoupanca(0, 0.5)
cp1.depositar(1000)
cp1.calcular_rendimento()