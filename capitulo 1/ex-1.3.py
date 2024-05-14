# Exercício 1.3  :: Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distintas. Em seguida, imprima a média aritmética dos três números.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))
num3 = float(input("Digite mais um número: "))

media = (num1 + num2 + num3) / 3

print(f"A média aritmética dos 3 números digitados é: {media}")
