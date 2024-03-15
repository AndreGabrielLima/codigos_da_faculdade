opcao = input()
matriz = []
soma = 0
quant = 0

for i in range(12):
    l = []
    for j in range(12):
        l.append(float(input()))

    matriz.append(l)

for i in range(5):
    selec_matriz = matriz[i][i+1:12-i-1]
    soma += sum(selec_matriz)
    quant += len(selec_matriz)

if opcao == 'M':
    print('{:.1f}'.format(soma/quant))
else:
    print('{:.1f}'.format(soma))