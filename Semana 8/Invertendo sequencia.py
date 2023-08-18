itens = []

while True:
    item = input("Digite um número inteiro(ou '0' para sair): ")
    if item.lower() == '0':
        break
    try:
        numero = int(item)
        itens.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

print("Itens digitados na ordem intersa:")
for item in reversed(itens):
    print(item)
