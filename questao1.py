soma = 0
quant = 10
lista = []

for i in range(1, 11):
    notas = float(input())
    soma += notas

    if notas < 7:
        lista.append(i)

print('{:.2f}'.format(soma/quant))
print('{}'.format(lista), end='')