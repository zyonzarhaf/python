ti = int(input('Informe o valor do primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
nt = int(input('Deseja saber o valor de quantos termos da PA? '))
c = 1
tc = ti
print('Com esses valores os 10 primeiros termos da PA são:')
while c <= nt:
    print(tc, end=' ')
    tc = tc + r
    c = c + 1
print('\n{:#^40}'.format('FIM!'))
