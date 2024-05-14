# Exercício 9.4  :: Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada.

class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$ {:.2f} realizado. Saldo atual: R$ {:.2f}".format(valor, self.saldo))
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print("Saque de R$ {:.2f} realizado. Saldo atual: R$ {:.2f}".format(valor, self.saldo))

conta = ContaBancaria()
conta.depositar(1000)

try:
    conta.sacar(500)
    conta.sacar(700) 
except SaldoInsuficienteError as e:
    print("Erro:", e)
