# Exercício 4.27  :: Faça um programa que crie um objeto datetime representando um instante específico. Em seguida, adicione 2 dias e 5 horas a esse instante utilizando timedelta.

from datetime import datetime, timedelta

instante_especifico = datetime(2024, 5, 12, 10, 30, 0) 

print("Instante específico:", instante_especifico)

novo_instante = instante_especifico + timedelta(days=2, hours=5)

print("Novo instante após adicionar 2 dias e 5 horas:", novo_instante)
