pessoas = [
    {
        'nome':'Fulano',
        'idade':20,
        'profissao':'programador'
    },
    {
        'nome':'Cicrano',
        'idade':25,
        'profissao':'cientista'
    },
    {
        'nome':'Beltrano',
        'idade':30,
        'profissao':'gerente de projetos'
    }
]

for i in range(len(pessoas)):
    print(f'Índice: {i + 1}:')
    print(f'Nome: {pessoas[i]['nome']}')
    print(f'Idade: {pessoas[i]['idade']}')
    print(f'Profissão: {pessoas[i]['profissao']}\n')