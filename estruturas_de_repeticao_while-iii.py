n1 = int(input('Informe um valor numérico: '))
n2 = int(input('Informe um segundo valor numérico: '))
escolha = 0
continuar = ' '
while escolha != 5:
    print('{:#^40}'.format('MENU DE OPÇÕES'))
    escolha = int(input('''[1] Somar
    [2] Multiplicar
    [3] Determinar o maior valor
    [4] Informar novos números
    [5] Sair\n'''))
    if escolha == 1:
        r = n1 + n2
        print('{} + {} = {}'.format(n1, n2, r))
    elif escolha == 2:
        r = n1 * n2
        print('{} x {} = {}'.format(n1, n2, r))
    elif escolha == 3:
        if n1 > n2:
            print('{} é o maior valor.'.format(n1))
        elif n2 > n1:
            print('{} é o maior valor.'.format(n2))
        else:
            print('{} e {} são iguais'. format(n1, n2))
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente.')
print('{:#^40}'.format('Fim da execução do programa.'))