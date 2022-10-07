import math

pontoXA = int(input('Digite o ponto XA: '))
pontoYA = int(input('Digite o ponto YA: '))
pontoXB = int(input('Digite o ponto XB: '))
pontoYB = int(input('Digite o ponto YB: '))
dX = math.pow((pontoXB - pontoXA), 2)
dY = math.pow((pontoYB - pontoYA), 2)
dAb = math.sqrt(dX + dY)
print('A distância entre os dois pontos é: %f' % dAb)
