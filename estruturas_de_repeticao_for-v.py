s = 0
for c in range(6, 0, -1):
    n = int(input('Digite um número qualquer: '))
    if n % 2 == 0:
        s = s + n
if s == 0:
    print('Nenhum valor par encontrado')
else:
    print('A soma de todos os valores pares digitados é igual a {}'.format(s))
print('####FIM!####')