opcao = input()
matriz = []
soma = 0
quant = 0

for i in range(12):
    l = []
    for j in range(12):
        l.append(float(input))

    matriz.append(l)

for i in range(12):
    for j in range(12):
        if j > i :
            soma += matriz[i][j]
            quant += 1

if opcao == 'm':
    print('{:.1f}'.format(soma/quant))
else:
    print('{:.1f}'.format(soma))