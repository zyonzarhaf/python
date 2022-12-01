lista = []
for c in range (0, 5):
    add = int(input('Digite qualquer valor numérico: '))
    while add in lista:
        add = int(input('Esse valor já está na lista, digite outro diferente: '))
    lista.append(add)
for c in range (0, len(lista)):
    for d in range (0, len(lista) - 1):
        if lista[d] > lista[d+1]:
            swap = lista[d+1]
            lista[d+1] = lista[d]
            lista[d] = swap
print(lista)