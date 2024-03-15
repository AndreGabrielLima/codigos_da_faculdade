valor = int(input())
fibonacci1 = 0
fibonacci2 = 1
sequencia = [0,1]

for i in range(0, 61):
    fibonacci = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci

    sequencia.append(fibonacci)

for i in range(0, valor):
    n = int(input())
    print('Fib({}) = {}'.format(n, sequencia[n]))