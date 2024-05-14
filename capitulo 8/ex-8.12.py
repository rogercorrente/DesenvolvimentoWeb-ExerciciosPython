# Exercício 8.12  :: Crie uma classe chamada Veiculo com métodos para acelerar, frear e exibir a velocidade do veículo. Crie uma classe chamada Carro que herde da classe Veiculo e adicione um atributo chamado marca. Crie uma instância da classe Carro e teste os métodos criados.

class Veiculo:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade -= valor
    
    def exibir_velocidade(self):
        print("Velocidade:", self.velocidade)

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca

meu_carro = Carro("Toyota")

meu_carro.acelerar(50)
meu_carro.exibir_velocidade()
meu_carro.frear(20)
meu_carro.exibir_velocidade()
