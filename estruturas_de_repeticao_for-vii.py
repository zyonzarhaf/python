### le um numero inteiro e diz se é primo
tot = 0
n = int(input('Digite um número qualquer: '))
for c in range (1, n + 1, 1):
    if n % c == 0:
        tot = tot + 1
if tot == 2:
    print('{} é divisivel por {} vezes em um intervalo de 1 a {} e por isso é um número primo.'.format(n, tot, n))
else:
    print('{} é divisivel por {} vezes em um intervalo de 1 a {} e por isso não é um número primo.'.format(n, tot, n))