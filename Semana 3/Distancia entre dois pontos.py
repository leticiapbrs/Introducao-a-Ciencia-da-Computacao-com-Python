import math

x1 = int(input("Insira a coordenada x de um plano cartesiano: "))
y1 = int(input("Insira a coordenada y de um plano cartesiano: "))
x2 = int(input("Insira a coordenada x de um outro ponto do mesmo plano: "))
y2 = int(input("Insira a coordenada y de um outro ponto do mesmo plano: "))

distancia = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

if distancia >= 10:
        print("longe")
else:
        print("perto")
