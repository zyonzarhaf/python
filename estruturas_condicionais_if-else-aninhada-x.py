#Conversor de bases numéricas
n = int(input('Digite qualquer número: '))
print('''Escolha uma das opções abaixo para realizar a conversão de base numérica:
[1] Para binário 
[2] Para octal 
[3] Para hexadecimal''')
b = int(input(': '))
if b == 1:
    print('Convertido para binário é igual a {}'.format(bin(n)[2:]))
elif b == 2:
    print('Convertido para octal é igual a {}'.format(oct(n)[2:]))
elif b == 3:
    print('Convertido para hexadecimal é igual a {}'.format(hex(n)[2:]))
else:
    print('Opção inválida!')
print('FIM!')