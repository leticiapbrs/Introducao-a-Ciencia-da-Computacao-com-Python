n = int(input("Digite um numero inteiro: "))

eh_primo = True

for i in range (2, n):
    if n % i == 0:
        eh_primo = False
        

if eh_primo:
    print("primo")
else:
    print("não primo")




        
