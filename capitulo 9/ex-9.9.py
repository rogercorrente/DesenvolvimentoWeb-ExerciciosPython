# Exercício 9.9  :: Crie uma função chamada read_file que recebe o nome de um arquivo como argumento e imprime o conteúdo do arquivo. A função deve abrir o arquivo para leitura no bloco try, tratar exceções no bloco except para o caso do arquivo não existir, e finalmente fechar o arquivo no bloco finally, independente de exceções terem sido lançadas ou não.

def read_file(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    finally:
        if 'arquivo' in locals():
            arquivo.close()

read_file("arquivo.txt")

read_file("arquivo.txt")
