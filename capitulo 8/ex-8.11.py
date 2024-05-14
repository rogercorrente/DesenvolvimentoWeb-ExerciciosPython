# Exercício 8.11  :: Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa. Crie um método chamado mostrar_dados que exiba o nome e a idade da pessoa. Crie uma classe chamada Funcionario que herde da classe Pessoa e adicione um atributo chamado salario. Crie um método chamado aumentar_salario na classe Funcionario que receba um valor de aumento e adicione ao salário atual. Crie uma instância da classe Funcionario, chame o método aumentar_salario com um valor de aumento de 10% e chame o método mostrar_dados.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumentar_salario(self, aumento):
        self.salario += aumento * self.salario / 100

funcionario1 = Funcionario("João", 30, 5000)

funcionario1.aumentar_salario(10)

funcionario1.mostrar_dados()
