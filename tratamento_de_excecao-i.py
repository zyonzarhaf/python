int("string")

try:
    int("string")
except ValueError:
    print('Não é possível converter uma string para inteiro!')