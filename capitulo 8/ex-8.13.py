# Exercício 8.13  :: Crie uma classe chamada ContaBancaria com métodos para depositar, sacar e consultar o saldo da conta. Crie uma classe chamada ContaPoupanca que herde da classe ContaBancaria e adicione um atributo chamado taxa_juros, que corresponde à taxa de juros mensal. Em seguida, crie um método chamado rendimento na classe ContaPoupanca que calcule o rendimento mensal da conta, dado um número de meses como parâmetro. Crie uma instância da classe ContaPoupanca com uma taxa de juros de 0,5%, faça um depósito de R$ 1.000,00 e calcule o rendimento de 12 meses.


class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print("Saldo atual:", self.saldo)

class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros
    
    def rendimento(self, num_meses):
        for _ in range(num_meses):
            self.saldo += self.saldo * (self.taxa_juros / 100)

conta_poupanca = ContaPoupanca(0.5)
conta_poupanca.depositar(1000)
conta_poupanca.rendimento(12)
conta_poupanca.consultar_saldo()
