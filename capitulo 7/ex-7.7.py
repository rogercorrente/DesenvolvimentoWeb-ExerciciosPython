# Exercício 7.7  :: Faça um programa que crie um diretório chamado "temp" e, dentro desse diretório, crie também um arquivo chamado "temp.txt".

import os

nome_diretorio = "temp"
nome_arquivo = "temp.txt"

os.makedirs(nome_diretorio)
print(f"Diretório '{nome_diretorio}' criado com sucesso.")

with open(os.path.join(nome_diretorio, nome_arquivo), 'w') as arquivo:
    print(f"Arquivo '{nome_arquivo}' criado dentro do diretório '{nome_diretorio}' com sucesso.")
