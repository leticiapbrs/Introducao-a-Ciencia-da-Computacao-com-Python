import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    x = -b/(2*a)
    print(f"a raiz dupla desta equação é {x}")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    if x1 < x2:
        print(f"as raízes da equação são {x1:.1f} e {x2:.1f}")
    else:
        print(f"as raízes da equação são {x2:.1f} e {x1:.1f}")
