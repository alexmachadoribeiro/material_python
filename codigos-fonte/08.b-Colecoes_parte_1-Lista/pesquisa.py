nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Fulano']
nome = input('Informe o nome que deseja encontrar: ')

quantidade = nomes_lista.count(nome)

try:
    print(f'{nome} foi encontrado na lista {quantidade} vezes.')
except:
    print(f'{nome} não foi encontrado.')