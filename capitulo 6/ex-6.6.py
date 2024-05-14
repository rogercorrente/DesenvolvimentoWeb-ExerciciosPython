# Exercício 6.6  :: Faça um programa que use dict comprehension para criar um dicionário com as raízes quadradas dos números de 1 a 10. Utilize os números como chave e as raízes quadradas como valor.

dicionario = {x:round(x**(1/2),3) for x in range(11) }
print(dicionario)