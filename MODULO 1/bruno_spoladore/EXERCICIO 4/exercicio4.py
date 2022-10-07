from modules import *
from tabulate import tabulate

erro = True
while erro:
    try:
        tamanho_vetor = int(input('Informe o tamanho lógico do vetor (25 até 100): '))
        if not 25 <= tamanho_vetor <= 100:
            raise ValueError('Tamanho inválido.')
        erro = False
        vetor = gera_vetor(tamanho_vetor)
        tabela_frequencia = frequencia(vetor)
        print(tabulate(tabela_frequencia, tablefmt='fancy_grid'))
    except ValueError as err:
        print(err)
