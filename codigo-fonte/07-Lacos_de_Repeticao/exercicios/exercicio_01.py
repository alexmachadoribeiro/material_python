'''
1. Crie um programa que receba 2 números do usuário, e que ele possa escolher um das 4 operações matemáticas para calcular os dois números. O programa deverá exibir na tela o resultado da conta matemática. O programa deverá dar também ao usuário uma opção para sair do programa caso deseje, e que ele possa fazer quantos cálculos desejar.
'''

while True:
    print("0 - Sair do programa.")
    print("1 - Somar dois números.")
    print("2 - Subtrair dois números.")
    print("3 - Multiplicar dois números.")
    print("4 - Dividir dois números.")

    opcao = input("\nOpção desejada: ")

    if opcao == "0":
        break
    elif opcao > 1 and opcao < 4:
        print("Opção inválida. Favor escolher outra opção")
        continue
    else:
        try:
            x = float(input("\nInforme o 1º número: "))
            y = float(input("Informe o 2º número: "))

            match opcao:
                case "1":
                    result = x+y
                    print(f"Resultado da soma é {result}.\n")
                    continue
                case "2":
                    result = x-y
                    print(f"Resultado da subtração é {result}.\n")
                    continue
                case "3":
                    result = x*y
                    print(f"Resultado da multiplicação é {result}.\n")
                    continue
                case "4":
                    result = x/y
                    print(f"Resultado da divisão é {result}.\n")
                    continue
        except Exception as e:
            print(f"Não foi possível realizar o cálculo.\n{e}")
            break