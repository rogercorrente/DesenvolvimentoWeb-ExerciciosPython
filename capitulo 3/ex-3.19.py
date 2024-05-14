# Exercício 3.19  :: Crie um programa que verifique se uma palavra digitada pelo usuário é um palíndromo. Se for, imprimir, ao final, "A palavra é um palíndromo". Se não for, imprimir "A palavra não é um palíndromo".

palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
