#Simula um radar de velocidade, informando se o veículo ultrapassou a máxima permitida e quanto ficou a multa
print('#######RADAR DE VELOCIDADE#######')
vmax = float(80+(20/100*80))
multa = float(7.00)
vdetectada = int(input('Velocidade do veículo: '))
if vdetectada > vmax:
    print('Veículo multado por exceder a velocidade máxima permitida')
    multado = (vdetectada - vmax) * 7.00
    print('Valor da multa: R${}'.format(multado))
else:
    print('Veículo está trafegando na velocidade permitida')
print('###############FIM###############')