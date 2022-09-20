#Analise de condições para concessão de empréstimo
c = float(input('Informe o valor da casa: R$'))
s = float(input('Informe o salário do comprador: '))
a = int(input('Quantos anos de financiamento? '))
prestacao = c / (a*12)
min = 30 /100 * s
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(c, a, prestacao))
if prestacao > min:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('Empréstimo pode ser concedido.')