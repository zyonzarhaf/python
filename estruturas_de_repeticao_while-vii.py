s = 0
qtd_n = 0

while True:
    n = int(input('Digite alguns valores numéricos (999 para parar): '))
    if n == 999:
        break
    s = s + n 
    qtd_n = qtd_n + 1
print(f'Você digitou {qtd_n} valores e a soma entre eles é {s}')
print('{:#^40}'.format('FIM!'))