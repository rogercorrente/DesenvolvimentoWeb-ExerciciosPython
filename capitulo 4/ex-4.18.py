# Exercício 4.18  :: Faça um programa que crie um objeto time que represente a hora atual.

from datetime import datetime

hora_atual = datetime.now().time()

print("Hora atual:", hora_atual)
