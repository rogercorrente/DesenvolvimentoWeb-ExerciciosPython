# Exercício 9.7  :: Crie uma classe Triangulo com os atributos lado1, lado2 e lado3. Implemente um método tipo_triangulo que informe se o triângulo é equilátero, isósceles ou escaleno. Utilize tratamento de exceções para lidar com triângulos inválidos.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_triangulo(self):
        try:
            # Verificando se os lados formam um triângulo válido
            if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
                # Verificando se é equilátero
                if self.lado1 == self.lado2 == self.lado3:
                    return "Equilátero"
                # Verificando se é isósceles
                elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                    return "Isósceles"
                else:
                    return "Escaleno"
            else:
                return "Triângulo inválido"
        except TypeError:
            return "Erro: Por favor, insira apenas valores numéricos para os lados do triângulo."

triangulo1 = Triangulo(5, 5, 5)
print("Triângulo 1:", triangulo1.tipo_triangulo())

triangulo2 = Triangulo(3, 4, 5)
print("Triângulo 2:", triangulo2.tipo_triangulo())

triangulo3 = Triangulo(5, 5, 10)
print("Triângulo 3:", triangulo3.tipo_triangulo())

triangulo4 = Triangulo("a", 5, 5)
print("Triângulo 4:", triangulo4.tipo_triangulo())
