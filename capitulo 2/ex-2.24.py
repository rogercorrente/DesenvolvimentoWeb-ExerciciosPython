# Exercício 2.24  :: Escreva um programa que peça ao usuário para inserir uma faixa etária e, em seguida, utilize a estrutura match..case para sugerir um filme adequado para essa idade. Você pode categorizar as faixas etárias e sugerir diferentes tipos de filmes para cada categoria, como filmes infantis para crianças, ação para adolescentes, drama para adultos etc.

def sugerir_filme(faixa_etaria):
    match faixa_etaria:
        case "0-10":
            print("Sugestão: Toy Story")
        case "11-17":
            print("Sugestão: Senhor dos Anéis")
        case "18-25":
            print("Sugestão: A Rede Social")
        case "26-35":
            print("Sugestão: Interestelar")
        case "36-49":
            print("Sugestão: O Poderoso Chefão")
        case "50+":
            print("Sugestão: O Exótico Hotel Marigold")
        case _:
            print("Faixa etária não reconhecida.")

faixa_etaria = input("Insira sua faixa etária (ex: 0-10, 11-17, 18-25, 26-35, 36-49, 50+): ")

sugerir_filme(faixa_etaria)
