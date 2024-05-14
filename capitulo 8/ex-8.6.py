# Exercício 8.6  :: Crie uma classe chamada Circulo com um método __init__ que inicialize o raio do círculo. Crie um método chamado area que retorne a área do círculo. Crie uma instância da classe Circulo e chame o método area.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2

meu_circulo = Circulo(5)

print("Área do círculo:", meu_circulo.area())
