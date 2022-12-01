lista = []
maior = 0
menor = 0
for c in range (0, 5):
    lista.append(int(input('Digite um valor: ')))
    if lista[c] > maior:
        maior = lista[c]
    if c == 0:
        menor = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
print(f'Temos os valores', end=' ')
for c in lista:
    print(c, end=' ')
print(f'na lista, sendo {maior} na posição {lista.index(maior)} o maior valor e {menor} na posição {lista.index(menor)} o menor valor.')