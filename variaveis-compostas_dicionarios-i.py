#estrutura de dados nao ordenados
#são identificados por chaves/keys {} e funcionam como se fossem indices de listas, mas com algumas peculiaridades. EX:
dados = dict() #ou dados = {}
dados = {'Nome': 'Pedro', 'Idade': 21}

print(dados) #mostra na tela a estrutura 'dados', incluindo todas as keys e seus respectivos valores (keys+valores = items)
print(dados['Nome']) #mostra na tela o valor da key 'nome'(que seria o "indice" do valor 'pedro', como nas listas) da estrutura 'dados'
print(dados['Idade']) #msm coisa

#diferentemente das listas, o metodo append não funciona nos dicionarios. A adição de keys e seus respectivos valores funciona assim:
dados['Estado Civil'] = 'Solteiro'
print(dados)
print(dados['Estado Civil'])

#deletar keys e seus respectivos valores:
del dados['Idade']
print(dados)

#colocar dicionarios dentro de uma lista
lista = list() #ou lista = []
dados1 = dict()

for c in range (0,3):
    dados1['Nome'] = str(input('Nome: '))
    dados1['Idade'] = int(input('Idade: '))
    lista.append(dados1.copy()) #semelhante a copia de listas por pass. de par. por valor usando o [:]
print(lista)
for d in lista:
    for k, v in d.items():
        print(f'{k}: {v}')
