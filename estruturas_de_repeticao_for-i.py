### mostra na tela uma contagem regressiva, indo de 10 até 1, c/ uma pausa de 1s entre cada contagem
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FIM')