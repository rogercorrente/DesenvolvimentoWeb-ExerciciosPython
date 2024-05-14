# Exercício 7.5  :: Crie um arquivo vazio qualquer. Agora, na mesma pasta, crie um programa que solicite ao usuário que digite o nome desse arquivo e exclua-o.


import os

nome_arquivo = input("Digite o nome do arquivo a ser excluído: ")

os.remove(nome_arquivo)
print(f"O arquivo '{nome_arquivo}' foi excluído com sucesso.")

