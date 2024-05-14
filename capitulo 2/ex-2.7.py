# Exercício 2.7  :: Crie um programa que verifique se um texto digitado pelo usuário é um número inteiro ou não e mostre uma mensagem de acordo (use texto.isdigit() para verificar).

texto = input("Digite um texto: ")

if texto.isdigit():
    print("O texto digitado é um número inteiro.")
else:
    print("O texto digitado não é um número inteiro.")
