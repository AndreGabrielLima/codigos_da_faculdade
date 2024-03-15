while True:
    number = int(input())
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'não é primo')
                break
        else:
            print(number, 'é primo')
    print('Digite 0 pra finalizar ou 1 pra continuar')
    if int(input()) == 0:
        break