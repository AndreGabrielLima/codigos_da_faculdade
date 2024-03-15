num_par = 0
num_impar = 0
num_posi = 0
num_neg = 0
cont = 0

while (cont < 5):
    x = int(input())
    if (x % 2 == 0):
        num_par += 1
    if (x % 2 != 0):
        num_impar += 1
    if (x > 0):
        num_posi +=1
    if (x < 0):
        num_neg += 1
    cont += 1

print('{} valor(es) par(es)'.format(num_par))
print('{} valor(es) impar(es)'.format(num_impar))
print('{} valor(es) positivo(s)'.format(num_posi))
print('{} valor(es) negativo(s)'.format(num_neg))