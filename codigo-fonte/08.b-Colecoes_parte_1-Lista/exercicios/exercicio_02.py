'''
2. Crie um programa que o usuário possa digitar quantos números digitar, e ao terminar, imprima os números em ordem crescente.
'''

numeros = []

try:
    while True:
        novo_numero = int(input("Informe um número inteiro ou pressione 'Enter' para encerrar o programa: "))

        if novo_numero:
            numeros.append(novo_numero)
            print("Número inserido com sucesso!")
            continue
        else:
            break
except Exception as e:
    print(f"Não foi possível inserir o número na lista.\n{e}")
finally:
    numeros.sort()
    print(numeros)