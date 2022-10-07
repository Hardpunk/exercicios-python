from random import *

numero_aleatorio = randint(0, 100)
tentativas = 1
continua_jogando = True

while continua_jogando:
    if tentativas <= 20:
        erro = True
        print('Tentativa %d' % tentativas)
        while erro:
            try:
                chutar_numero = int(input('Informe um número entre 0 e 100: '))
                if 0 <= chutar_numero <= 100:
                    erro = False
                else:
                    raise ValueError()
            except ValueError as err:
                print('Insira somente números entre 0 e 100')

        tentativas += 1
        if chutar_numero > numero_aleatorio:
            print('Errou. Tente um número menor.')
            continue
        elif chutar_numero < numero_aleatorio:
            print('Errou. Tente um número maior.')
            continue
        elif chutar_numero == numero_aleatorio:
            print('Parabéns, você acertou o número!\nTentativas: %d' % tentativas)
    else:
        print('Limite de tentativas excedido. Voce perdeu!')

    tentativas = 1
    jogar_novamente = ''
    numero_aleatorio = randint(0, 100)
    while jogar_novamente != 'n' and jogar_novamente != 's':
        jogar_novamente = input('Gostaria de jogar novamente? (s/n)').lower()
        if jogar_novamente == 'n':
            continua_jogando = False
        elif jogar_novamente != 'n' and jogar_novamente != 's':
            print('Opção inválida. Insira apenas "s" ou "n".')
