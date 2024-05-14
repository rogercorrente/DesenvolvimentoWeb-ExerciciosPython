# Exercício 6.7  :: Faça um programa que crie um dicionário com nomes e notas de alunos, ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. Em seguida, use dict comprehension para criar um dicionário com os alunos e suas notas arredondadas para o número inteiro mais próximo da nota do aluno.

def criar_dicionario_notas() -> dict:
    dicionario_notas = dict()
    while True:
        nome_aluno = input("Digite o nome do aluno (ou -1 para sair):\n")
        nota_aluno = float(input("Digite a nota do aluno:\n"))
        if nome_aluno == "-1":
            break
        else:
            dicionario_notas[nome_aluno] = nota_aluno
    dicionario_notas_arredondadas = {aluno: round(nota) for aluno, nota in dicionario_notas.items()}
    return dicionario_notas_arredondadas

print(criar_dicionario_notas())
