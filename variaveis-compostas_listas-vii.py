listaO = []
listaP = []
listaI = []
while True:
    listaO.append(int(input('Digite um valor numérico: ')))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(listaO):
    if v % 2 == 0:
        listaP.append(v)
    elif v % 2 != 0:
        listaI.append(v)
print(f'=-'*42)
print(f'A lista completa é {listaO}')
print(f'A lista contendo somente valores pares é {listaP}')
print(f'A lista contendo somente valores impares é {listaI}')
print(f'Fim!')