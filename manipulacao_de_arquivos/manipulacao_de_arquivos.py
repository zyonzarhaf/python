###le um arquivo

arquivo = open('caminho/arquivo.txt', 'r')
arquivo.readline() #le a proxima linha
arquivo.readlines() #le todas as linhas restantes
arquivo.close()

###escreve em um arquivo

with open('caminho/arquivo.txt', 'w') as arquivo_w:
    arquivo_w.write('um texto qualquer\n')