lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Primeira forma

for i in range(len(lista)):
    if (lista[i] % 2 == 0):
        lista[i] *= 2
        print('Índice {} atualizado para o valor {}'.format(i, lista[i]))

# Segunda forma

print('Lista final:')
for elemento in lista:
    print('Número {}'.format(elemento))