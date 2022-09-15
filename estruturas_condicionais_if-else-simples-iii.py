print('#######RADAR DE VELOCIDADE#######')
vmax = int(80+(20/100*80))
multa = float(7.00)
vdetectada = int(input('Velocidade do veículo: '))
if vdetectada > vmax:
    print('Veículo multado por exceder a velocidade máxima permitida')
    multado = (vdetectada - vmax) * 7.00
    print('Valor da multa: R${}'.format(multado))
else:
    print('Veículo está trafegando na velocidade permitida')
print('###############FIM###############')