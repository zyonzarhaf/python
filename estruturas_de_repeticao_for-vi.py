### lê o primeiro termo e a razão de uma PA, para em seguida mostrar na tela seus 10 primeiros termos
n1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
n2 = 0
r = int(input('Agora digite a razão da progressão aritmética: '))
print(n1)
for c in range(0, 10, 1):
    n2 = n1 + r
    print(n2)
    n1 = n2
print('####FIM!####')