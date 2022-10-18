from itertools import count


tupla = ('Joao', 'Marcos', 'Felipe', 'Lucas', 'Maria',
         'Fernanda', 'Camila', 'Janaina', 'Antonio')
print(tupla[0:6]) #mostra os cinco primeiros nomes
print(tupla[-4:]) #mostra os quatro ultimos nomes
print(sorted(tupla)) #mostra os nomes em ordem alfabetica
print(tupla)
print(tupla.index('Fernanda')) #mostra a posição/index do elemento 'Fernanda'