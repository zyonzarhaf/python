#jogo da adivinhação v2
import random

chutes = 0
print('Vou pensar em um número de 1 a 10. Tente adivinhá-lo.')
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha = random.choice(list)
resposta = int(input('Qual número eu escolhi? '))
while resposta != escolha:
    chutes = chutes + 1
    if resposta < escolha:
        resposta = int(input('Errou! Tente de novo, mas dessa vez tente chutar um valor mais alto... '))
    elif resposta > escolha:
         resposta = int(input('Errou! Tente de novo, mas dessa vez tente chutar um valor menor... '))
    else:
        resposta = int(input('Errou! Tente de novo, foi uma jogada bem mais ou menos... '))
print('Pensei no número {}, acertou com {} tentativas!\n####FIM!####'.format(escolha, chutes))