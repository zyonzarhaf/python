from random import randint
from time import sleep

print('{:=^40}'.format(' JokenPÔ! '))
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Faça sua jogada:
[0] Pedra
[1] Papel
[2] Tesoura''')
opção_jogador = int(input(''))
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('PÔ!')
sleep(0.5)
print('-='*20)
print('Você jogou {}'.format(itens[opção_jogador]))
maquina = randint(0, 2)
print('A máquina jogou {}'.format(itens[maquina]))
print('-='*20)
if maquina == 0:
    if opção_jogador == 0:
        print('EMPATE!')
    elif opção_jogador == 1:
        print('Você venceu!')
    elif opção_jogador == 2:
        print('A máquina venceu!')
elif maquina == 1:
    if opção_jogador == 0:
        print('A máquina venceu!')
    elif opção_jogador == 1:
        print('EMPATE!')
    elif opção_jogador == 2:
        print('Você venceu!')
elif maquina == 2:
    if opção_jogador == 0:
        print('Você venceu!')
    elif opção_jogador == 1:
        print('A máquina venceu!')
    elif opção_jogador == 2:
        print('EMPATE!')
print('FIM DO JOGO!')