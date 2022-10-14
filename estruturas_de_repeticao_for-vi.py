### lê o primeiro termo e a razão de uma PA, para em seguida mostrar na tela seus 10 primeiros termos
n1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Agora informe a razão da PA: '))
n10 = n1 + (10-1) * r
for c in range(n1, n10 + r, r):
    print('{}'.format(c), end=' ')
print('\n####FIM!####')