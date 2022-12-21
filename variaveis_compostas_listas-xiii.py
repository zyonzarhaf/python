ficha = []

continuar = 'S'

while continuar not in 'N':
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida. Por favor, informe se deseja continuar [S/N]: ')).upper().strip()

print(ficha)
print(f'{"No":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if opc == 999:
        break
    elif opc <= len(ficha):
        print(f'Nome: {ficha[opc][0]}, notas {ficha[opc][1][0]} e {ficha[opc][1][1]}')
print('FIM!')