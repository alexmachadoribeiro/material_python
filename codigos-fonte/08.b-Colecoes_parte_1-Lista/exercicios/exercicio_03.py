'''
3. Crie um programa que o usuário possa digitar uma quantidade desejada de notas de um determinado aluno (nota mínima 0 e nota máxima 10), e o programa calcula a média desse aluno, e ao final informe se o aluno está aprovado ou reprovado (média mínima para aprovação = 7).
'''

notas = []

try:
    while True:
        print("1 - Inserir nota")
        print("2 - Calcular média e encerrar o programa")

        opcao = input("Opção desejada: ")

        match opcao:
            case "1":
                nova_nota = float(input("Informe a nota do aluno de 0 a 10: "))

                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print("Nota inserida com sucesso!")
                else:
                    print("Nota inválida.")

                continue
            case "2":
                media = sum(notas)/len(notas)
                resultado = "aprovado" if media >= 7 else "reprovado"

                print(f"Média: {media:.2f}.\nO aluno está {resultado}.")

                break
except Exception as e:
    print(f"Não foi possível executar a operação.\n{e}")