### mostra a soma entre todos os numeros impares que são múltiplos de três e que se encontram no intervalo de 1 até 500
s = 0
for c in range(1, 501, 3):
    if c % 2 != 0:
        s = s + c
print(s)
print('####FIM!####')