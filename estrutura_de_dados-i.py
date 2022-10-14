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

###dicionarios sao estruturas compostas de chaves e valores -- tb podem ser dividas em items, sendo q cada item é uma 'chave':valor

dicionario = {'a': 1, 'b': 2}   ###cria um dict com duas chaves ('a' e 'b', com os valores 1 e 2, respectivamente --nesse caso sao numeros, mas normalmente utilizam-se strings)
print(dicionario)
dicionario['c'] = 3              ###adiciona uma chave e um valor associado
print(dicionario)
del dicionario['c']
print(dicionario)                ###deleta uma chave