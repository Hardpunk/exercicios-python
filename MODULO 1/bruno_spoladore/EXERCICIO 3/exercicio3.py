from modules import sdata

data_valida = False

while not data_valida:
    try:
        dia = int(input('Insira o dia: '))
        mes = int(input('Insira o mês: '))
        ano = int(input('Insira o ano: '))
        data_valida = sdata(dia, mes, ano)
    except ValueError as err:
        print(err)
    else:
        if data_valida:
            print(data_valida)
