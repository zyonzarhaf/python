from random import randint

continuar = ' '
while continuar not in 'N':
    inicio_jogador = int(input('Escolha um valor de 1 a 10: '))
    inicio_maquina = randint(0, 10)
    tot = inicio_jogador + inicio_maquina
    vez_jogador = str(input('Vai jogar par ou impar? ')).strip().upper()[0]
    print(f'Você jogou {inicio_jogador} e a máquina jogou {inicio_maquina}, totalizando {tot}.')
    if tot % 2 == 0:
        print('Deu par!')
    else:
        print('Deu impar!')
    if vez_jogador == 'P':
        if tot % 2 == 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
    elif vez_jogador == 'I':
        if tot % 2 != 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
    continuar = str(input('Quer jogar de novo? [S/N] ')).strip().upper()[0]