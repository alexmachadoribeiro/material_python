nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
altura = float(input("Informe a altura em metros: "))

if idade >= 12 and altura >= 1.2:
    print(f'A entrada de {nome} está autorizada.')
else:
    print(f'A entrada de {nome} não está autorizada.')