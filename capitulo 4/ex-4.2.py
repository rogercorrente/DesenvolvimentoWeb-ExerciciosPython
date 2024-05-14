# Exercício 4.2  :: Crie um programa que peça ao usuário para inserir um número e calcule a raiz quadrada desse número. Ao fim, mostre o número como um valor monetário do Brasil.

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

numero = float(input("Digite um número: "))

raiz_quadrada = numero ** 0.5

print(f"A raiz quadrada de {numero} é {locale.currency(raiz_quadrada, grouping=True)}")
