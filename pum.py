n = int(input())
cont=1
for _ in range(n):
    for _ in range(4):
        if cont % 4 != 0:
            print(cont, end=' ')
        else:
            print('PUM')
        cont += 1
