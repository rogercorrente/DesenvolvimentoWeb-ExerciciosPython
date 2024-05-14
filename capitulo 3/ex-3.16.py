# Exercício 3.16  :: Crie um programa que encontre e mostre o maior e o menor número em uma lista de 10 números digitada pelo usuário.

numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
