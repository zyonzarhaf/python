#Calcula o preço de uma passagem, cobrando 0.50 reais por km para viagens de até 200 km e 0.45 para viagens de mais de 200 km.
d = int(input('Qual a distância em km da sua viagem? '))
if d <= 200:
    p = float(0.50)
    print('Sua viagem custará R${}.'.format(p * d))
else:
    p = float(0.45)
    print('Sua viagem custará R${}.'.format(p * d))
print('FIM!')