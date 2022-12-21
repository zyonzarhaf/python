from random import randint
lista_j = []
lista_n = []
print('=-'*30)
qtd_j = int(input('Quantos jogos você deseja sortear? '))
qtd_n = int(input('Informe a quantidade máxima de números para cada sorteio: '))
print('=-'*30)
for c in range (0, qtd_j):
    cont = 0
    while cont < qtd_n:
        palpite = randint(1,60)
        if palpite not in lista_n:
            lista_n.append(palpite)
            cont = cont + 1
    lista_j.append(lista_n[:])
    lista_n.clear()
for c in range (0, qtd_j):
    print(f'{c + 1}o jogo: {lista_j[c]}')