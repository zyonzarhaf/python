c = 3
t1 = 0
t2 = 1

print('{:#^40}'.format('Sequência Fibonacci'))
print('=-'*20)
qtd_termos = int(input('Quantos termos deseja exibir na tela? '))
print(t1, end=' ')
print(t2, end=' ')
while c <= qtd_termos:
    t3 = t1 + t2
    print('{}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    c = c + 1
print('\n','=-'*20)
print('{:#^40}'.format('FIM!'))