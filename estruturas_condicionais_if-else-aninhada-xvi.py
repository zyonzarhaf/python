print('{:=^40}'.format(' IMC '))
peso = float(input('Informe seu peso atual (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / altura ** 2
print('Seu Indice de Massa Corporal (IMC) é de {}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
print('FIM!')