n = input("Digite uma sequência de números: ")
n = list(map(int, n.split()))

for num in n:
    fatorial = 1
    i = 1
    while i <= num:
        fatorial *= i
        i += 1
    print(f'O fatorial de {num} é {fatorial}')
