N = int(input())
soma = 0
matriz = []

for i in range(N):
    l = []
    for j in range(N):
        l.append(int(input()))

    matriz.append(l)

sum_diagonal = sum(matriz[i][i] for i in range(N))

ds = []

for i in range(N):
    for j in range(N):
        if i + j == N - 1:
            ds.append(matriz[i][j])

for i in range(N):
    for j in range(N):
        if j % 2 != 0:     
            soma += matriz[i][j]



sum_secun = sum(ds)

print(sum_diagonal)
print(sum_secun)
print(soma)