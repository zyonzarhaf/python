### escreve um dicionario em um arquivo txt, csv e json
import json

dicionario = {'Nome': 'Fulano', 'Data de nascimento': 'dia/mês/ano', 'Endereço': 'Rua, Bairro, Cidade, Estado'}
with open('manipulacao_de_arquivos/exercicio-i.txt', 'w') as arquivo_w:
    arquivo_w.write(json.dumps(dicionario))