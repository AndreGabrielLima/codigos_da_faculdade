n = int(input())
opcao = input()

matriz = []

soma = 0

for i in range(12):
    l = []
    for j in range(12):
        entrada_de_dados = float(input())
        l.append(entrada_de_dados)
    
    matriz.append(l)

for i in range(12):
    soma += matriz[i][n]

if opcao == 'M':
    print('{:.1f}'.format(soma/12))

else:
    print('{:.1f}'.format(soma))