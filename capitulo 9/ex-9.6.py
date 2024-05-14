# Exercício 9.6  :: Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. Utilize tratamento de exceções para garantir que o usuário insira apenas números válidos.

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 10): "))
            if tentativa < 1 or tentativa > 10:
                raise ValueError("Por favor, insira um número entre 1 e 10.")
            
            tentativas += 1

            if tentativa == numero_secreto:
                print("Parabéns! Você acertou o número secreto {} em {} tentativas.".format(numero_secreto, tentativas))
                break
            else:
                print("Tente novamente!")

        except ValueError as e:
            print("Erro:", e)

# Iniciando o jogo
jogo_adivinhacao()
