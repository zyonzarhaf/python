exp = str(input('Digite uma expressão matemática: '))
teste = []
for c in exp:
    if c == '(':
        teste.append('(')
    elif c == ')':
        if len(teste) > 0:
            teste.pop()
        else:
            teste.append(')')
            break
if len(teste) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')