'''
1. Crie um programa que possa incluir, pesquisar, alterar e excluir nomes em uma lista, que pode ter quantos nomes o usuário desejar.
'''

nomes = []

while True:
    print(f'{'-' * 30} CRUD {'-' * 30}\n')
    print('1 - Inserir nome.')
    print('2 - Listar nomes.')
    print('3 - Pesquisar por um nome.')
    print('4 - Ordenar nomes.')
    print('5 - Atualizar um nome.')
    print('6 - Deletar um nome.')
    print('7 - Sair do programa.')

    opcao = int(input('Informe a opção desejada: '))

    match opcao:
        case 1:
            novo_nome = input('Novo nome: ')
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.\n')
            continue
        case 2:
            for i in range(len(nomes)):
                print(f'ID: {i + 1} - {nomes[i]}')
            print('')
            continue
        case 3:
            pesquisa_nome = input('Pesquisar nome: ')
            quantidade = nomes.count(pesquisa_nome)
            try:
                print(f'Encontrado {quantidade} vezes: {pesquisa_nome}\n')
            except:
                print(f'{pesquisa_nome} não encontrado.\n')
            continue
        case 4:
            nomes.sort()
            print('Ordenação feita com sucesso.\n')
            continue
        case 5:
            id_nome = int(input('Informe o ID do nome a ser alterado: '))
            if id_nome > 0 and id_nome < len(nomes):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            nomes[id_nome] = input('Informe o novo nome: ')
            print(f'Nome do ID {id_nome + 1} alterado com sucesso.\n')
            continue
        case 6:
            id_nome = int(input('Informe o ID do nome a ser excluído: '))
            if id_nome > 0 and id_nome < len(nomes):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            del(nomes[id_nome])
            print(f'Nome deletado com sucesso.\n')
            continue
        case 7:
            break
        case _:
            print('Opção inválida.\n')
            continue