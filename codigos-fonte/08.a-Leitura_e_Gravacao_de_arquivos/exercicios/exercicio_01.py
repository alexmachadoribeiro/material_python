'''
1. Crie um programa em que o usuário possa escolher se deseja ler o arquivo, gravar dados no arquivo, ou sair do programa.
'''

while True:
    print('0 - Sair do programa.')
    print('1 - Ler arquivo.')
    print('2 - Gravar novos dados no arquivo.')

    opcao = input('Opção desejada: ')

    match opcao:
            case "0":
                break
            case '1':
                with open("dados.txt", 'r', encoding="utf-8") as arquivo:
                    dados = arquivo.read()
                print(f'\n{dados}\n')
                continue
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input("Insira o nome do novo usuário: ")
                nova_idade = input("Insira a idade do novo usuário: ")
                nova_profissao = input("Insira a profissão do novo usuário: ")
                dados += f'\n\n{'-'*30}\n\nNome: {novo_nome}.\nIdade: {nova_idade}.\nProfissão: {nova_profissao}.'
                with open('dados.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.write(dados)
                continue
            case _:
                print('Opção inválida')
                continue