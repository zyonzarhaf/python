#Jogo simples de adivinhação
import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhá-lo.')
list = [0, 1, 2, 3, 4, 5]
# tb funcionaria com var = randint(0, 5)
escolha = random.choice(list)
resposta = int(input('Qual número eu escolhi? '))
if resposta == escolha:
     print('Você acertou!')
else:
    print('Errado, era o número {}.'.format(escolha))