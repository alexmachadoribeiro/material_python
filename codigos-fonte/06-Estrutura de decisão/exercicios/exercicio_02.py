'''
2. Um elevador de carga possui capacidade para 200 kg. Crie um programa que receba do usuário o peso da carga, e verifica se a carga está autorizada a usar o elevador ou não.
'''

try:
    nome = input("Informe o seu nome: ")
    carga = float(input("Informe a carga em kg: "))

    verificacao = "está acima" if carga > 200 else "está abaixo"

    print(f"A carga transportada por {nome} {verificacao} da capacidade máxima do elevador.")
except Exception as e:
    print(f"Não foi possível verificar o peso da carga.\n{e}")