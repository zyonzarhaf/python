# mostra se uma frase é um palindromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range (len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
print(junto, inverso)
if inverso == junto:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')