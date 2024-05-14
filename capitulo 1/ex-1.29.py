# Exercício 1.29  :: Crie um programa que tenha um dicionário com os nomes, idades e cor dos olhos de 5 membros da sua família. Cada item do dicionário deve ter o nome da pessoa como chave e uma tupla associada contendo a idade e a cor dos olhos.

# Criando um dicionário com os nomes, idades e cor dos olhos dos membros da família
familia = {
    "Roger": (23, "castanhos"),
    "Valesca": (23, "castanhos"),
    "Rejane": (57, "verdes"),
    "Roarim": (71, "castanhos"),
    "Luzia": (78, "verdes")
}

for nome, dados in familia.items():
    idade, cor_olhos = dados
    print(f"Nome: {nome}, Idade: {idade}, Cor dos olhos: {cor_olhos}")
