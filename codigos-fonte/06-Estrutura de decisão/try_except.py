valor1 = '10'
valor2 = 10

try:
    print(valor1 + valor2)
except Exception as e:
    print(f'Não foi possível rodar o programa. {e}.')
finally:
    print('Tente mudar o valor da variável "valor1" para um número inteiro caso dê erro.')