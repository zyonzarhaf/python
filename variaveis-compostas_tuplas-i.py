tupla_e = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito')

continuar = ' '
while continuar not in 'N':
    while True:
        tupla_input = int(input('Digite um numero de 0 a 8: '))
        if 0 <= tupla_input <= 8:
            break
        print('Valor excedeu o limite, tente novamente.')
    print(f'Você digitou o número {tupla_e[tupla_input]}')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('{:#^40}'.format('FIM!'))