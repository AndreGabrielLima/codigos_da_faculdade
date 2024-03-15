n = int(input())
for _ in range(n):
    soma = 0
    x, y = input().split()
    x = int(x)
    y = int(y)

    for i in range(y * 2):
        if x % 2 != 0:
            soma += x
            x += 1
        else:
            x += 1
    print(soma)