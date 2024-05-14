# Exercício 9.3  :: Implemente uma calculadora que realize operações de soma, subtração, multiplicação e divisão. Utilize tratamento de exceções para lidar com operações inválidas.

def calcular():
    try:
        # Solicitando ao usuário a operação desejada
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        operacao = int(input("Digite o número da operação desejada: "))

        # Solicitando os números de entrada
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realizando a operação selecionada
        if operacao == 1:
            resultado = num1 + num2
            print("Resultado:", resultado)
        elif operacao == 2:
            resultado = num1 - num2
            print("Resultado:", resultado)
        elif operacao == 3:
            resultado = num1 * num2
            print("Resultado:", resultado)
        elif operacao == 4:
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Operação inválida.")

    except ValueError:
        print("Erro: Por favor, digite apenas números.")
    except ZeroDivisionError as e:
        print("Erro:", e)

# Chamando a função principal
calcular()
