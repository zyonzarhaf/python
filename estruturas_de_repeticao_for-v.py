### le seis numeros inteiros e mostra a soma somente dos valores pares
r = 0
s = 0
for c in range(6, 0, -1):
    n = int(input('Digite um número qualquer: '))
    if n % 2 == 0:
        r = r + 1
        s = s + n
print('Você digitou {} valores pares e a soma entre eles foi {}.'.format(r, s))