from random import *
import math


def frequencia(vetor):
    tabela_frequencia = []
    tamanho_vetor = len(vetor)
    n = math.sqrt(tamanho_vetor)
    maior_numero = max(vetor)
    menor_numero = min(vetor)
    amplitude = math.ceil((maior_numero - menor_numero) / n)
    qtd_total_elementos = 0
    i = 0
    print('Amplitude: %d' % amplitude)
    print('Vetor: %s' % vetor)
    while i < math.ceil(n):
        qtd_elementos = 0
        limite_inferior = menor_numero + (i * amplitude)
        limite_superior = limite_inferior + amplitude
        for x in vetor:
            if limite_inferior <= x < limite_superior:
                qtd_elementos += 1
        qtd_total_elementos += qtd_elementos
        i += 1
        tabela_frequencia.append([limite_inferior, limite_superior, qtd_elementos])
    return tabela_frequencia


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
