nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Fulano']

try:
    indice = int(input("Informe o índice que deseja alterar: "))
    nomes_lista[indice] = input("Informe o novo nome: ")

    for nome in nomes_lista:
        print(nome)
except Exception as e:
    print(f"Não foi possível alterar o nome.\n{e}")