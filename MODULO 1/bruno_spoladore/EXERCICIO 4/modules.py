from random import *
import math


def frequencia(vetor):
    n = math.sqrt(len(vetor))
    maior_numero = max(vetor)
    menor_numero = min(vetor)
    amplitude = math.ceil((maior_numero - menor_numero) / n)


def gera_vetor(tamanho_vetor):
    vetor = []
    for i in range(0, tamanho_vetor):
        numero_aleatorio = randint(1, 100)
        numero_existe = numero_aleatorio in vetor
        while numero_existe:
            numero_aleatorio = randint(1, 100)
            numero_existe = numero_aleatorio in vetor

        vetor.append(numero_aleatorio)

    vetor.sort()
    return vetor
