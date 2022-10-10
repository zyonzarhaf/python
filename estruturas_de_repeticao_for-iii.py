### mostra a soma entre todos os numeros impares que são múltiplos de três e que se encontram no intervalo de 1 até 500
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s = s + c
print('\nA soma entre todos esses valores é igual a {}.'.format(s))