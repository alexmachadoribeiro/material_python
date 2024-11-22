lista_itens = []

while True:
    item = input('Insira um item, ou deixe em branco para terminar a lista: ')

    if item != '':
        lista_itens.append(item)
        continue
    else:
        break

for item in lista_itens:
    print(item)