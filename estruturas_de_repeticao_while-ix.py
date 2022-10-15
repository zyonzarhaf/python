masc = mai18 = fem20menor = 0

while True:
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
    resp = str(input('Cadastro realizado! Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{mai18} pessoas com mais de 18 anos, {masc} homens e {fem20menor} mulheres com menos de 20 anos foram cadastradas.')
print('{:#^40}'.format('FIM!')) 