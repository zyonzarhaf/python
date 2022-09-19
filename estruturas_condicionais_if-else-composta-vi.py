#Informa se um ano é bissexto
a = (int(input('Informe um ano qualquer: ')))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto.')
print('FIM!')