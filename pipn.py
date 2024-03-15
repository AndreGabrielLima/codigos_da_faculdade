contPosi = 0
contNeg = 0
contImp = 0 
contPa = 0

for i in range(5):
    x = int(input())
    if x > 0:
        contPosi += 1
    elif x < 0:
        contNeg += 1
    if x % 2 == 0:
        contPa += 1
    else:
        contImp += 1

print('{} valor(es) par(es)'.format(contPa))
print('{} valor(es) impar(es)'.format(contImp))
print('{} valor(es) positivo(s)'.format(contPosi))
print('{} valor(es) negativo(s)'.format(contNeg))