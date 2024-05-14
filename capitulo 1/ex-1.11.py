# Exercício 1.11  :: Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

raio = float(input("Digite o raio do círculo: "))

pi_aproximado = 3.14159  # Aproximação do valor de pi

area = pi_aproximado * raio ** 2
comprimento = 2 * pi_aproximado * raio

print(f"A área do círculo é: {area}")
print(f"O comprimento do círculo é: {comprimento}")
