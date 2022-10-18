print(f'{"-"}'*58)
print(f'{"Contador de vogais":^58}')
print(f'{"-"}'*58)
tupla = ('Carro','Escola','Baralho','Empresa','Aviao','Chocolate','Cachorro','Computador',
'Programa','Propriedade','Montanha','Academia',)
for c in tupla:
    print(f'\nNa palavra {c} temos', end=' ')
    tot = 0
    for d in c:
        if d.lower() in 'aeiou':
            tot = tot + 1
            print(f'{d}', end=' ')
    print(f', totalizando {tot} vogais')
print(f'\n{"FIM!":-^58}')