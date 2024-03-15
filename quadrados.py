n = int(input())

for i in range(1, n + 1): # o 'n + 1' é para pegar o valor também digitado
    if i % 2 == 0:
        print('{}^2 = {}'.format(i, i ** 2))