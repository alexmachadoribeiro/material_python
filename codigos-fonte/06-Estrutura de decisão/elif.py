nome = input("Informe o nome: ")
nota = int(input("Informe a nota: "))

if nota >= 7:
    print(f'{nome} foi aprovado.')
elif nota >= 5:
    print(f'{nome} está de recuperação.')
else:
    print(f'{nome} está reprovado.')