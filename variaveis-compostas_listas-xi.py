pares = impares = scol = maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)

for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range (0,3):
    for c in range (0,3):
        if matriz[l][c] % 2 == 0:
            pares = pares + matriz [l][c]
        elif matriz [l][c] % 2 != 0:
            impares = impares + matriz [l][c]

for l in range (0,3):
    scol = scol + matriz[l][2]

for c in range (0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma de todos os valores pares digitados é {pares}.')
print(f'A soma de todos os valores impares digitados é {impares}.')
print(f'A soma de todos os elementos na terceira coluna é {scol}.')
print(f'O maior valor encontrado na segunda linha é {maior}.')
