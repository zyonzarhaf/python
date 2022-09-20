preço = float(input('Preço total das compras: R$'))
print('''Escolha uma forma de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão (sem juros)
[4] 3x ou mais no cartão (com juros de 20%''')
opção = int(input(''))
if opção == 1:
    total = preço - (10/100*preço)
    print('Total: {}'.format(total))
elif opção == 2:
    total = preço - (5/100*preço)
    print('Total: {}'.format(total))
elif opção == 3:
    total = preço
    totparcelas = preço / 2
    print('Sua compra será parcelada em 2x de R${}, totalizando R${} (sem juros).'.format(totparcelas, total))
elif opção == 4:
    parcelas = int(input('Em quantas parcelas deseja efetuar a compra?'))
    total = preço + (20/100*preço)
    totparcelas = total / parcelas
    print('Sua compra será parcelada em {}x de R${}, totalizando R${}.'.format(parcelas, totparcelas, total))
else:
    print('Opção inválida!')
print('FIM!')