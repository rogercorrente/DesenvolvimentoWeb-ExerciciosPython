# Exercício 3.13  :: Crie um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
