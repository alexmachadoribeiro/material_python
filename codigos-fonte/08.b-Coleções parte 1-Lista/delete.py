nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana']

posicao = int(input('Informe a posição do item que deseja excluir: '))

try:
    del(nomes_lista[posicao])
except:
    print('Não foi possível deletar.')

for nome in nomes_lista:
    print(nome)