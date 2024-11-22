'''
2. Crie um programa que liste 5 salas de cinema, e mostre os filmes de cada uma das salas e suas classificações indicativas. O usuário deverá informar sua idade e a sala com o filme desejado. Caso o usuário tenha a idade mínima para ver o filme, o programa irá imprimir o ingresso para o filme desejado. Caso o usuário não tenha a idade mínima, o programa deverá informar que ele não tem idade para ver o filme, e deverá retornar a lista de filmes para que o usuário escolha outro filme.
'''

try:
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe sua idade: "))

    while True:
        print("\nLISTA DE FILMES:\n")
        print("Sala 1: A Roda Quadrada - Livre.")
        print("Sala 2: A Volta dos Que Não Foram - 12 anos.")
        print("Sala 3: Poeira em Alto Mar - 14 anos.")
        print("Sala 4: As Tranças do Rei Careca - 16 anos.")
        print("Sala 5: A Vingança do Peixe Frito - 18 anos.")

        sala = input("\nInforme a sala desejada: ")

        match sala:
            case "1":
                idade_minima = 0
                filme = "A Roda Quadrada"
            case "2":
                idade_minima = 12
                filme = "A Volta dos Que Não Foram"
            case "3":
                idade_minima = 14
                filme = "Poeira em Alto Mar"
            case "4":
                idade_minima = 16
                filme = "As Tranças do Rei Careca"
            case "5":
                idade_minima = 18
                filme = "A Vingança do Peixe Frito"
            case _:
                print("Sala inexistente. Favor selecionar outra sala.")
                continue

        if idade >= idade_minima:
            print(f"Ingresso liberado para {nome}.\nSala: {sala}. Filme: {filme}.\nTenha um bom filme!\n")
            break
        else:
            print(f"Ingresso não liberado.\n{nome} não possui a idade mínima para ver o filme.\nFavor escolher outra sala.\n")
            continue
except Exception as e:
    print(f"Não foi possível selecionar o filme.\n{e}")