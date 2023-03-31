import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0 :
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: ", raiz1)
else:
    if delta < 0:
        print("Essa equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)
