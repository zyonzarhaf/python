n1 = int(input('Qual a largura da parede que deseja pintar? '))
n2 = int(input('E a altura? '))
a = n1*n2
l = 2
print('A área da parede (altura vezes largura) é igual a {}m^2 e o litro de tinta pinta uma área de até 2m^2. Isso significa que você deve usar {} litros de tinta para pintar a parede.'.format(a, a/2))