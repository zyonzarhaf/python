nome_aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Informe a primeira nota de {}: '.format(nome_aluno)))
nota2 = float(input('Informe a segunda nota de {}: '.format(nome_aluno)))
m = (nota1 + nota2) / 2
print('A média de {} é de {}.'.format(nome_aluno, m))
if m >= 5 and m < 7:
    print('Resultado: RECUPERAÇÃO.')
elif m < 5:
    print('Resultado: REPROVADO.')
elif m > 7:
    print('Resultado: APROVADO!')
print('FIM!')