import locale
from datetime import datetime
from calendar import isleap

locale.setlocale(locale.LC_ALL, 'pt_BR')


def sdata(dia, mes, ano):
    try:
        data_extenso = '%d/%d/%d' % (dia, mes, ano)
        data_formatada = datetime.strptime(data_extenso, '%d/%m/%Y')
        mes_extenso = datetime.strftime(data_formatada, '%B')
        if mes in (1, 3, 5, 7, 8, 10, 12) and not (1 <= dia <= 31):
            raise ValueError('Dia inválido para o mês de %s.' % mes_extenso)
        elif mes in (4, 6, 9, 11) and not (1 <= dia <= 30):
            raise ValueError('Dia inválido para o mês de %s.' % mes_extenso)
        elif isleap(ano) and mes == 2 and not (1 <= dia <= 29):
            raise ValueError('Dia inválido para o mês de %s.' % mes_extenso)
        elif mes == 2 and not (1 <= dia <= 28):
            raise ValueError('Dia inválido para o mês de %s.' % mes_extenso)
    except ValueError as err:
        print(err)
        return False
    else:
        dia = datetime.strftime(data_formatada, '%d')
        ano = datetime.strftime(data_formatada, '%Y')
        return '%s de %s de %s' % (dia, mes_extenso, ano)
