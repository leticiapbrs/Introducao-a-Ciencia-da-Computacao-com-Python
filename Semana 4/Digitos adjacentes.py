n = input("Digite um numero inteiro: ")

adjacentes_iguais = False

for i in range (1, len(n)):
    if n[i] == n[i-1]:
        adjacentes_iguais = True
        break

if adjacentes_iguais:
    print("sim")
else:
    print("não")
