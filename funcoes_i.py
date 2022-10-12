def fibonacci(n):                    ###declara a funcao fibonacci tendo uma variavel n como parametro
    a, b = 0, 1                     ###a recebe 0, b recebe 1 (1o termo = 0, 2o termo = 1)
    while a < n:                    ###estrutura de repeticao
        print(a, end=' ')           ###printa o primeiro termo
        a, b = b, a + b             ###o primeiro recebe o segundo, o segundo recebe a soma entre o primeiro e o segundo /\ *repete*, originando os termos seguintes
    print()

fibonacci(100)
fibonacci(200)
fibonacci(300)
fibonacci(400)
fibonacci(500)