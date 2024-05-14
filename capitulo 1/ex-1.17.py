# Exercício 1.17  :: Crie um programa que peça ao usuário para digitar a velocidade inicial, a velocidade final e o tempo de transição de uma velocidade para a outra. Em seguida, o programa deve calcular e mostrar a aceleração.


velocidade_inicial = float(input("Digite a velocidade inicial (m/s): "))
velocidade_final = float(input("Digite a velocidade final (m/s): "))
tempo_transicao = float(input("Digite o tempo de transição (s): "))

aceleracao = (velocidade_final - velocidade_inicial) / tempo_transicao

print(f"A aceleração é: {aceleracao} m/s^2")
