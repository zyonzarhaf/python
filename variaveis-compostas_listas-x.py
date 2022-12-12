total = [[], []]

for c in range(1, 8):
    valores = int(input(f'Digite o {c}o valor: '))
    if valores % 2 == 0:
        total[0].append(valores)
    elif valores % 2 != 0:
        total[1].append(valores)
total[0].sort()
print(f'Os valores pares digitados foram: {total[0]}')
total[1].sort()
print(f'Os valores impares digitados foram: {total[1]}')