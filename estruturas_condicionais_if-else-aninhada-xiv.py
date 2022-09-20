from datetime import date

ano_atual = date.today().year
nome_atleta = str(input('Informe o nome do atleta: '))
nasc_atleta = int(input('Informe a data de seu nascimento: '))
idade_atleta = ano_atual - nasc_atleta
print('Nome do atleta: {}. Idade: {}. Ano atual: {}.'.format(nome_atleta, idade_atleta, ano_atual))
if idade_atleta <= 9:
    print('Categoria pela qual irá competir: MIRIM.')
elif idade_atleta > 9 and idade_atleta <= 14:
    print('Categoria pela qual irá competir: INFANTIL.')
elif idade_atleta > 14 and idade_atleta <= 19:
    print('Categoria pela qual irá competir: JUNIOR.')
elif idade_atleta > 19 and idade_atleta <= 25:
    print('Categoria pela qual irá competir: SÊNIOR.')
else:
    print('Categoria pela qual irá competir: MASTER.')
print('FIM!')