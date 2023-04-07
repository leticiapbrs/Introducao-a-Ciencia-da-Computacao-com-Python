largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
    
while altura > 0:
    largura_atual = largura
    while largura_atual > 0:
        print("#", end="")
        largura_atual = largura_atual - 1
    print()
    altura = altura - 1
