# Exercício 8.18  :: Crie uma classe chamada Animal com um método __init__ que inicialize o nome do animal. Crie um método chamado emitir_som que emita um som genérico do animal. Crie uma classe chamada Cachorro que herde da classe Animal e adicione um método chamado emitir_som que emita o som do latido do cachorro. Crie uma instância da classe Cachorro e chame o método emitir_som.

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print("O animal emite um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro late: Au au!")

meu_cachorro = Cachorro("Rex")

meu_cachorro.emitir_som()
