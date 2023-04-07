

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n   
    for i in range(m, 0, -1):
        if (n - i) % (m + 1) == 0:
            print("O computador tirou", i, "peças.")
            return i   
    print("O computador tirou", m, "peças.")
    return m

def usuario_escolhe_jogada(n, m):
    jogada = int(input("\nQuantas peças você vai tirar?"))
    while jogada > m or jogada <= 0:
        print("\nOops! Jogada inválida! Tente de novo.")
        jogada = int(input("\nQuantas peças você vai tirar?"))
    print("\nVocê tirou", jogada, "peças.")
    return jogada        

jogador_ganhou = 0
computador_ganhou = 0
    
def partida():
    n = 0
    m = 0
    while n <= 0:
        n = int(input("Quantas peças?" ))
        if n <= 0:
            print("Número de peças inválido. Tente novamente.")
    while m <= 0 or m >= n:
        m = int(input("Limite de peças por jogada?"))
        if m <= 0 or m>n:
            print("Limite inválido. Tente novamente")   
    if n%(m+1) == 0:
        print("\nVocê começa!")
        vez_do_usuario = True
    else:
        print("\nComputador começa!")
        vez_do_usuario = False   
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print("Agora resta", n, "peças no tabuleiro.\n")
            vez_do_usuario = False
            if n <= 0:
                print("Fim de jogo! Você ganhou!")
                global jogador_ganhou
                jogador_ganhou += 1
                break
        else:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n > 1:
                print("Agora resta", n, "peças no tabuleiro.")
            vez_do_usuario = True
            if n <= 0:
                print("Fim de jogo! O computador ganhou!")
                global computador_ganhou
                computador_ganhou += 1
                break

def campeonato():
    tipo_partida = int(input("Bem-vindo ao jogo do NIM! Escolha:\n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato \n"))
    if tipo_partida == 1:
        print("Você escolheu uma partida isolada \n")
        partida()
    elif tipo_partida == 2:
        print("Você escolheu um campeonato \n")
        for i in range(1,4):
            print("**** Rodada", i, "****")
            partida()   
    else:
        print("Comando inválido. Tente novamente")
        tipo_partida = int(input("Bem-vindo ao jogo do NIM! Escolha:\n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato \n"))
        return tipo_partida
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você", jogador_ganhou, "X", computador_ganhou, "Computador")

campeonato()


    
    
