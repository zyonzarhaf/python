n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print('A soma entre os valores digitados é {}, o produto é {} e a divisão é {}'.format(s, m, d), end = ' ')
print('A divisão inteira é {} e o resto é {}. n1 elevado a potência de n2 é {}'.format(di, r, e))
