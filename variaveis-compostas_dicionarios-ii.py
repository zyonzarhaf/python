dados = {}

while True:
    dados['Nome'] = str(input('Nome do aluno: '))
    dados['Média']= int(input('Media do aluno: '))
    if dados['Média'] < 60:
        dados['Situaçao'] = 'REPROVADO'
    elif dados['Média'] >= 60:
        dados['Situaçao'] = 'APROVADO'
    for k, v in dados.items():
        print(f'{k}: {v}.', end=' ')
    print('\n')
    continuar = str(input('Continuar? [S/N] ')).upper().strip()
    if continuar in 'N':
        break