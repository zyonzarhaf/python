lista = [1, 2, 3, 4, 5]            ###declara a lista
print(lista)
lista.append(6)                    ###insere o numero 6 na lista
print(lista)
lista.remove(1)                    ###remove o numero 1 da lista
print(lista)


lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(set(lista))                  ###retira valores duplicados da lista

listaSduplicados = set(lista)      ###ou
print(listaSduplicados)

listaSduplicados = set([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
print(listaSduplicados)

dicionario = {'a': 1, 'b': 2}
print(dicionario)
dicionario['c'] = 3              ###adiciona um valor e uma posição
print(dicionario)
del dicionario['c']
print(dicionario)                ###deleta uma posicao