lista = [1, 2, 3, 4]
print(lista)
lista.append(5) #adiciona o elemento 5 a lista
print(lista)
lista.insert(4, 0) #adiciona o elemento 0 na posicao indicada (0 = elemento, 4 = posicao)
print(lista)
lista[3] = 2 #substitui o elemento 3 pelo elemento 2
print(lista)

############eliminar elementos
lista.pop(0) #remove somente o que estiver na posicao indicada, que no caso eh 0
print(lista)
lista.insert(0, 0)
print(lista)
lista.remove(0) #remove o conteudo indicado, que tb eh 0;
print(lista)
lista.insert(0, 0)
print(list)
del lista[0]
print(lista)

#######criar lista com range
lista = list(range(1,11))
print(lista)

###uteis
lista.sort ###ordena os elementos da lista
len(lista) ###comprimento da lista
enumerate(lista) ###pega index e valor
set(lista) ###remove duplicados da lista

###copia de listas
a = [1, 2, 3, 4, 5]
b = a[:] #pega todos os elementos de a.
print(a, b)