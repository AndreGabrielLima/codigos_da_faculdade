num1 = int(input())
while True:
    num2 = int(input())
    if num2 <= num1:
        print('Digite um valor maior que o primeiro!', end='')
        continue
    else:
        break


soma = 0
for i in range(num1, num2 + 1):    
    div = 0
    for c in range(1, i + i):
        if i % c == 0:
            div += 1
    if div < 3:
        soma += i

if soma == 0:
    print('Sem numeros primos no intervalo informado', end='')    
else:
    print(soma, end='')