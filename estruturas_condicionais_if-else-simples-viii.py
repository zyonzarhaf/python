#Informa se três retas podem ou não formar um triângulo
l1 = float(input('Informe o comprimento da 1a reta: '))
l2 = float(input('Informe o comprimento da 2a reta: '))
l3 = float(input('Informe o comprimento da 3a reta: '))
if l1 > abs(l2 - l3) and l1 < l2 + l3 or l2 > abs(l1 - l3) and l2 < l1 + l3 or l3 > abs(l1 - l2) and l3 < l1 + l2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
print('FIM!')