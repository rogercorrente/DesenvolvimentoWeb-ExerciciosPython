# Exercício 5.5  :: Crie uma função que defina uma variável x dentro da função e imprima o valor de x na tela. Em seguida, fora da função, crie uma linha de comando para imprimir o valor de x e analise o erro que será gerado ao tentar executar o programa.

def minha_funcao():
    x = 10
    print("Valor de x: ", x)

minha_funcao()

print("valor de x: ", x)

#o erro ocorre porque a variável x está definida dentro da função e não está acessível fora dela.