sala = int(input('Informe o número da sala de 1 a 5:'))

match sala:
    case 1:
        print('Filme: A Volta dos Que Não Foram.')
    case 2:
        print('Filme A Roda Quadrada.')
    case 3:
        print('Filme Poeira em Alto Mar.')
    case 4:
        print('Filme As Tranças do Rei Careca.')
    case 5:
        print('Filme A Vingança do Peixe Frito.')
    case _:
        print('Sala inexistente.')