n = int(input('Digite um número qualquer: '))
c = n
f = 1
print('{}! = {}'.format(n, c), end=' X ')
while c > 1:
    f = f * c
    c = c - 1
    print('{}'.format(c), end=' ')
    print('X ' if c > 1 else '= ', end='')
print(f)