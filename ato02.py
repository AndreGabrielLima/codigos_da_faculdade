maior = 0
soma_maior = 0

for i in range(5):
    soma = 0
    n = int(input())
    
    for i in range(1, n + 1):
        resto = n % i
        if resto == 0:
            soma += i
            if soma > soma_maior:
                soma_maior = soma
                maior = i
print(maior, end='')