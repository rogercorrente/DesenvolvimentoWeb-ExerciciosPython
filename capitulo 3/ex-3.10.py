# Exercício 3.10  :: Crie um programa que calcule e mostre todos os números primos de 1 a 100.

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("Números primos de 1 a 100:")
for numero in range(1, 101):
    if eh_primo(numero):
        print(numero)
