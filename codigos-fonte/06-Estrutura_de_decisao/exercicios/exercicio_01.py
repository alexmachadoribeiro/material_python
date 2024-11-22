'''
1. Crie um programa que calcule o **Índice de Massa Corporal (IMC)** do usuário, mostre o valor do IMC na tela, e retorne se o usuário está no peso ideal ou se precisa emagrecer ou engordar mais. Utilize a tabela do IMC para definir os valores.
'''

try:
    peso = float(input("Informe o peso em kg: "))
    altura = float(input("Informe a altura em metros: "))

    imc = peso/(altura**2)

    print(f"IMC do usuário é: {imc:.2f}.")

    if imc < 17:
        print("Você está muito abaixo do peso. Procure um médico.")
    elif imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está no seu peso ideal. Parabéns!")
    elif imc < 30:
        print("Você está acima do seu peso ideal.")
    elif imc < 35:
        print("Você está com Obesidade I.")
    elif imc < 40:
        print("Você está com Obesidade II.")
    else:
        print("Você está com Obesidade mórbida. Procure um médico.")
except Exception as e:
    print(f"Não foi possível calcular o IMC.\n{e}")