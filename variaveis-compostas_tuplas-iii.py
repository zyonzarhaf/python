from random import randint

maior = 0
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#print(f'Os valores gerados aleatoriamente na tupla foram: {tupla}.')
#ou
print('Os valores gerados aleatoriamente na tupla foram:', end=' ')
for c in tupla:
    print(c, end=' ')
for c in range (0, 4):
    if tupla[c] > maior:
        maior = tupla[c]
    c = c + 1
print(f'\nO maior valor aleatoriamente gerado na tupla é {maior}.')
#ou
#print(f'\nO maior valor aleatoriamente gerado na tupla é {max(tupla)}.')