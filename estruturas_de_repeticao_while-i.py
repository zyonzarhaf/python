### uma simples validação de dados
resposta = str(input('Informe seu sexo: ')).strip().upper()[0]
while resposta not in 'MF':
    resposta = str(input('Dado inválido. Por favor, informe corretamente seu sexo: ')).strip().upper()[0]
print('Dado registrado com sucesso.')
print('####FIM!####')