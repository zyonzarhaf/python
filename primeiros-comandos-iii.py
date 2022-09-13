n = input('Digite alguma coisa: ')
#teste de tipo
print('O tipo primitivo do valor digitado é um número? {}'.format(n.isnumeric()))
print('É um valor alfa? {}'.format(n.isalpha()))
print('É um valor alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
print('Pode aparecer na tela? {}'.format(n.isprintable()))