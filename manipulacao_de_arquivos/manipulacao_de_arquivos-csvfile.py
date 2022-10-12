### mesma coisa, mas utilizando um gerenciador de contexto

import csv

with open('manipulacao_de_arquivos/2021-07-08_15_43.csv', 'r') as csvfile:
    leitorcsv = csv.DictReader(csvfile)
    resultados = [linha for linha in csvfile]
    print(resultados)