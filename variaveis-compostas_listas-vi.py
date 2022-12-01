lista = []
quant = 0
while True:
    add = (int(input('Digite um valor qualquer: ')))
    while add in lista:
        add = (int(input(f'{add} já está na lista. Informe outro: ')))
    lista.append(add)
    quant = quant + 1
    for c in range (0, len(lista)):
        for d in range (0, len(lista) - 1):
            if lista[d] < lista[d+1]:
                swap = lista[d+1]
                lista[d+1] = lista[d]
                lista[d] = swap
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta in 'N':
        break
print(f'Você digitou {quant} valores e a lista em ordem decrescente ficou assim: ')
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')