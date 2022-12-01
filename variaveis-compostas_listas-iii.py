lista = []
while True:
    add = int(input('Digite um numero: '))
    while add in lista:
        add = int(input(f'{add} já está na lista. Informe um valor diferente: '))
    lista.append(add)
    continuar = str(input('Quer continuar? [s/n]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Por favor, informe se deseja continuar [s/n]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(lista)
print(sorted(lista))