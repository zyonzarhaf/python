total_compra = 0
maior_preco = 0
menor_preco = 0
c = 0

print('#' * 40)
print('         LOJA DE INFORMÁTICA')
print('#' * 40)
while True:
    continuar = ' '
    nome_produto = str(input('Nome do produto: '))
    preco_produto = int(input('Preço: R$'))
    c = c + 1
    total_compra = total_compra + preco_produto
    if preco_produto > maior_preco:
        maior_preco = preco_produto
        mais_caro = nome_produto
    if c == 1:
        menor_preco = preco_produto
        mais_barato = nome_produto
    else:
        if preco_produto < menor_preco:
            menor_preco = preco_produto
            mais_barato = nome_produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${total_compra}\n{mais_caro} foi o produto mais caro, custando R${maior_preco}\n{mais_barato} foi o produto mais barato, custando R${menor_preco}' if c != 1 else f'O total da compra foi R${total_compra}.')
print('{:#^40}'.format('FIM!'))