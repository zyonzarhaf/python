from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(0,6), 'Jogador 2': randint(0,6), 
'Jogador 3': randint(0,6), 'Jogador 4': randint(0,6)}
ranking = []

for k, v in jogo.items():
    print(f'{k} jogou {v} no dado')
    sleep(0.3)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(0.3)