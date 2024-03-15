voltas = int(input())
for voltasIndex in range(voltas):
    n1, n2 = input().split(' ')
    if len(n2) > len(n1):
        print('nao encaixa')
    elif n1[len(n1) -  len(n2) + len(n1)] == n2:
        print('encaixa')
    