# Exercício 7.8  :: Crie um programa que exclua o diretório criado no exercício anterior com todo o seu conteúdo (cuidado para não excluir a pasta errada).

import shutil

nome_diretorio = "temp"

shutil.rmtree(nome_diretorio)
print(f"Diretório '{nome_diretorio}' e todo o seu conteúdo foram excluídos com sucesso.")

