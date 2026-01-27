pessoa = {
    'Nome':'Alex Machado',
    'Idade':39,
    'Profissão':'Programador',
    'Empresa':'SENAI'
}

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')