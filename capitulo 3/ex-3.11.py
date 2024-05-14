# Exercício 3.11  :: Crie um programa que calcule e mostre todos os números entre 1 e 100 que possuem raiz quadrada exata.

print("Números com raiz quadrada exata de 1 a 100:")
for numero in range(1, 101):
    raiz_quadrada = numero ** 0.5
    if raiz_quadrada == int(raiz_quadrada):
        print(numero)
