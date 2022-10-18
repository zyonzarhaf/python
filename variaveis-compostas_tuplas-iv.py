par = 0

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(
    input('Digite um número: ')), int(input('Digite um número: ')))
if 9 in tupla:
    if tupla.count(9) > 1:
        print(f'O 9 aparece na tupla {tupla.count(9)} vezes.')
    else:
        print(f'O 9 aparece na tupla {tupla.count(9)} vez.')        
if 3 in tupla:
    print(f'Index do número 3 na tupla: {tupla.index(3) + 1}.')
print(f'Valores pares na tupla:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
print('\n{:#^}'.format('FIM!'))