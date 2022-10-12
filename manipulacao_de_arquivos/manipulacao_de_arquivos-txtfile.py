###le o arquivo txt e transforma seu conteudo p o formato de dicionario manualmente

txtfile = open('manipulacao_de_arquivos/2021-07-08_15_42.txt', 'r')
resultados = []
resultado = {}
for linha in txtfile.readlines():
    linha = linha.rstrip('\n')
    if linha:
        chave, valor = linha.split(': ')
        resultado[chave] = valor
    else:
        resultados.append(resultado)
        resultado = {}
print(resultados)
txtfile.close()