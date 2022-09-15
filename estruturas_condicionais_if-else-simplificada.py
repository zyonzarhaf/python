#Informa se um veículo do Paraná está isento de IPVA, usando a forma simplificada da condicional if else
print('#########ISENÇÃO DE IPVA NO PARANÁ#########')
t = int(input('Quantos anos de fabricação tem seu carro? '))
print('Seu carro está isendo de IPVA!' if t >= 20 else 'Seu carro ainda não está isento de IPVA.')
print('FIM')