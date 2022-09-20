from datetime import date

nasc = int(input('Informe a data de seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos de idade em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    qntfalta = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(qntfalta))
else:
    qntamais = idade- 18
    print('Você deveria ter se alistado há {} anos.'.format(qntamais))
print('FIM!')