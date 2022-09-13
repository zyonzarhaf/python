#sorteia um nome
import random
a1 = str(input('Digite o nome do 1o aluno: '))
a2 = str(input('Digite o nome do 2o aluno: '))
a3 = str(input('Digite o nome do 3o aluno: '))
a4 = str(input('Digite o nome do 4o aluno: '))
a5 = str(input('Digite o nome do 5o aluno: '))
list = [a1, a2, a3, a4, a5]
escolha = random.choice(list)
print('{} vai apagar a lousa.'.format(escolha))
#embaralha vários nomes
print('A ordem de apresentação será:')
random.shuffle(list)
print(list)