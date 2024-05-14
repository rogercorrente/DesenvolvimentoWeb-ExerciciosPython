# Exercício 5.4  :: Crie uma função que tenha dois parâmetros: nome e idade. A função deve imprimir na tela uma mensagem a seu gosto contendo o nome e a idade da pessoa. Em seguida, crie uma chamada para essa função passando argumentos de forma nomeada.

def imprimir_nome_idade(nome, idade):
    print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

imprimir_nome_idade(nome="Roger", idade=23)
