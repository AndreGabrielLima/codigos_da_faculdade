'''m = 0
lista = {}

for i in range(100):
    n = int(input())
    if n > m:
        m = n
        lista[n]

print(m)
print(lista[m] + 1)'''
maior = 0

for i in range(100):
    n = int(input())
    if n > maior:
        maior = n
        pos = i

print(maior)
print(pos + 1)