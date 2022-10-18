
tupla = ('Notebook', 3499, 
         'Monitor', 1999,
         'Mouse', 139, 
         'Mousepad', 99,
         'Pendrive', 32,
         'Pasta Termica', 15)
print(f'{"=-=" * 13}')
print(f'{"LISTA DE PRODUTOS":^40}')
print(f'{"=-=" * 13}')
for c in range (0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end='')
    else:
        print(f'R${tupla[c]:>7.2f}')
print(f'{"=-=" * 13}')