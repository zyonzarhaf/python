### mostra a tabuada de um número escolhido pelo usuário utilizando a estrutura de repeticao for
n = int(input('Quer saber a tabuada de qual número?'))
for c in range(1,11,1):
    print(n, 'x', c, '=', n*c)
print('####FIM!####')