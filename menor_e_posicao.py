valor = int(input())

valores = list(map(int, input().split()))

menorValor = min(valores)
menorPosi = 0

for i in range(valor):
    if valores[i] == menorValor:
        menorPosi = i

print('Menor valor: {}'.format(menorValor))
print('Posicao: {}'.format(menorPosi))