lista = [0]*20

for i in range(20):
    lista[i] = int(input())

lista.reverse()

for i in range(20):
    print(f'N[{i}] = {lista[i]}')

###################################################
# ou
###################################################
        
tamanho = 20
N = [0]*20

for i in range(tamanho):
    N[i] = int(input())

esquerda = 0 
direita = tamanho - 1

while esquerda < direita:
    N[esquerda], N[direita] = N[direita], N[esquerda]
    esquerda += 1
    direita -= 1

for i in range(tamanho):
    print(f'N[{i}] = {N[i]}')