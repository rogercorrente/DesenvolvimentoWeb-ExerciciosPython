# Exercício 6.14  :: Faça um programa que declare duas listas de mesmo tamanho, uma com 3 nomes de alunos e outra com 3 notas. Em seguida, usando a função zip() e list comprehension, retorne uma lista com as tuplas (nome, nota) em ordem decrescente de nota.

alunos = ['João', 'Maria', 'Pedro']
notas = [8.5, 7.2, 9.0]

tuplas_aluno_nota = list(zip(alunos, notas))

tuplas_ordenadas = sorted(tuplas_aluno_nota, key=lambda x: x[1], reverse=True)

print("Lista de alunos e notas em ordem decrescente de nota:")
for tupla in tuplas_ordenadas:
    print(tupla)
