with open("dados.txt", "r", encoding="utf-8") as f:
    dados = f.read()

print("Texto antes da gravação:\n")
print(dados)

novo_texto = input("Informe o texto a ser adicionado no arquivo: ")
nova_gravacao = f"{dados}\n{novo_texto}"

with open("dados.txt", "w", encoding="utf-8") as f:
    f.write(nova_gravacao)

with open("dados.txt", "r", encoding="utf-8") as f:
    dados = f.read()

print("\nTexto depois da gravação:\n")
print(dados)