while True:
    c = 1
    r = 0
    print('#' * 30)
    n = int(input('Quer a tabuada de qual valor? (999 para encerrar a execução do programa) '))
    print('#' * 30)
    if n == 999:
        break
    while c <= 10:
        r = n * c
        print(f'{n} X {c} = {r}')
        c = c + 1
print('{:#^30}'.format('FIM!'))