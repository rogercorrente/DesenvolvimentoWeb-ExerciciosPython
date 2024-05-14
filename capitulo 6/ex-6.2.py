# Exercício 6.2  :: Faça um programa que use list comprehension para criar uma lista com as palavras que contêm a letra "a" em uma frase digitada pelo usuário, substituindo a letra por "o".


frase = input("Digite uma frase: ")

palavra_substituida = [''.join(['o' if letra == 'a' else letra for letra in palavra]) for palavra in frase.split()]

print("Frase com letra a substituído por o:", ' '.join(palavra_substituida))


