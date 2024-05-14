# Exercício 4.9  :: Crie um programa que peça ao usuário para digitar um CPF e use uma expressão regular para verificar se o CPF está no formato DDD.DDD.DDD-DD, onde D corresponde a um dígito entre 0 e 9.

import re

padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

cpf = input("Digite um CPF (no formato XXX.XXX.XXX-XX): ")

if padrao_cpf.match(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
