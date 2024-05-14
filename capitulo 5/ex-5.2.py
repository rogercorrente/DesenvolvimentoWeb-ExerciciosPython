# Exercício 5.2  :: Crie uma função que tenha um número inteiro como parâmetro e retorne True se o número for par e False se o número for ímpar. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela.


def verificar_par(numero):
    return numero % 2 == 0

num1 = 10
num2 = 7

print(f"O número {num1} é par? {verificar_par(num1)}")
print(f"O número {num2} é par? {verificar_par(num2)}")
