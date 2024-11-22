cont = 0

while cont < 20:
    cont += 1
    if cont % 2 == 0:
        print(cont)
    elif cont < 5:
        ...
    elif cont >= 15:
        break
    else:
        continue

    print('Contando...')