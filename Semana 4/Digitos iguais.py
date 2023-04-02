n = input("Digite um numero inteiro: ")

numeros_unicos = set(n)

if len(numeros_unicos) < len(n):
    print("sim")
else:
    print("não")
        
