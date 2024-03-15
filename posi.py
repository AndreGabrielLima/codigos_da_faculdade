contPosi = 0
soma_positivo = 0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        contPosi += 1
        #soma_positivo += x
print('{} valores pares'.format(contPosi))
#print('{:.1f}'.format(soma_positivo / contPosi))
