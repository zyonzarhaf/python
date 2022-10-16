masc = 0
mai18 = 0
fem20menor = 0

while True:
    continuar = ' '
    print('#'*20)
    print('CADASTRE UMA PESSOA')
    print('#'*20)
    i = int(input('Informe a idade: '))
    s = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    print('#'*20)
    if i > 18:
        mai18 = mai18 + 1
    if s == 'M':
        masc = masc + 1
    if s =='F' and i < 20:
        fem20menor = fem20menor + 1
    while continuar not in 'SN':
        continuar = str(input('Cadastro realizado! Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos cadastradas: {mai18}.\nTotal de homens cadastrados: {masc}.\nTotal de mulheres com menos de 20 anos cadastradas: {fem20menor}.')
print('{:#^40}'.format('FIM!')) 