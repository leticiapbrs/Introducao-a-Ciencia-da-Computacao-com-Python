def maior_primo(n):
    for num in range(n, 1, -1):
        # Verifica se o número é primo
        eh_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            return num
    return None

# escreva maior_primo(número_limite_desejado ex 100) no console
