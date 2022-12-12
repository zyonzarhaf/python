temp = []
pessoas = []
pesados = []
leves = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso (kg): ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    continuar = input('Quer continuar? [S/N]').upper().strip()
    temp.clear()
    if continuar in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(pessoas)}.')
for p in pessoas:
    if p[1] == maior:
        pesados.append(p[0])
    if p[1] == menor:
        leves.append(p[0])
print(f'O maior peso foi de {pesados}, no valor de: {maior}kg')
print(f'O menor peso foi de {leves}, no valor de: {menor}kg')
print('=-'*42)