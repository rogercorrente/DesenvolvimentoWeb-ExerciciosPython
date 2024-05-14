# Exercício 4.14  :: Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, mostre a posição inicial de cada palavra contida nessa frase.

frase = input("Digite uma frase: ")

palavras = frase.split()

print("Posição inicial de cada palavra na frase:")
for palavra in palavras:
    posicao_inicial = frase.find(palavra)
    print(f"A palavra '{palavra}' começa na posição {posicao_inicial} na frase.")
