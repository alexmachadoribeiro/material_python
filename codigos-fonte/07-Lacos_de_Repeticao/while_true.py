while True:
    nome = input('Informe o seu nome ou deixe em branco para sair: ')

    if nome != '':
        idade = int(input('Informe sua idade: '))

        if idade >= 18:
            print(f'{nome} é maior de idade.')
        else:
            print(f'{nome} é menor de idade.')

        continue
    else:
        break