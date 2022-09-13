name = str(input('Digite o nome do aluno: '))
n1 = int(input('Digite a primeira nota de {}: '. format(name)))
n2 = int(input('Digite a segunda nota de {}: '.format(name)))
m = (n1 + n2) / 2
print('{} atingiu a média de {} pontos'.format(name, m))