### same, mas com gerenciador de contexto e try catch

import json

try:
    with open('manipulacao_de_arquivos/2021-07-08_15_43.json', 'r') as jsonfile:
        resultados = json.load(jsonfile)
except OSError:
        exit('Não foi possível abrir o arquivo.')
else:
        print(resultados)