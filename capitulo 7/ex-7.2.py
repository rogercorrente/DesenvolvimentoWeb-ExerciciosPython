# Exercício 7.2  :: Crie um programa que leia um arquivo texto e exiba quantas linhas ele possui.


nome_arquivo = input("Digite o nome do arquivo: ")

with open(nome_arquivo, 'r') as arquivo:
    num_linhas = sum(1 for linha in arquivo)
    print(f"O arquivo '{nome_arquivo}' possui {num_linhas} linhas.")

