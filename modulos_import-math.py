import math
#mostra a raiz quadrada de um número
n1 = int(input('Digite um número: '))
r = math.sqrt(n1)
print('A raiz de {} é igual a {:.2f}'.format(n1, r))
#mostra um número real truncado
n2 = float(input('Digite um valor real qualquer: '))
i = math.trunc(n2)
print('A porção inteira de {} é {}'.format(n2, i))
#mostra o comprimento da hipotenusa de um triângulo com base em seus catetos oposto e adjacente
cat_o = int(input('Informe o valor do cateto oposto: '))
cat_a= int(input('Agora informe o valor do cateto adjacente: '))
hipo = math.hypot(cat_o, cat_a)
print('A hipotenusa vale {}.'.format(math.trunc(hipo)))
#mostra o valor do seno, do cosseno e da tangente de um ângulo qualquer
n3 = int(input('Informe um ângulo qualquer: '))
s = math.sin(n3)
c = math.cos(n3)
t = math.tan(n3)
print('O seno de {} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}.'.format(n3, (s), (c), (t)))