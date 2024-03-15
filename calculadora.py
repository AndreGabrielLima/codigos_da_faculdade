while True:
    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))

        operacoes = ['Somar', 'Subtrair', 'Multiplicar', 'Dividir']

        for i, card in enumerate(operacoes):
            print('[{}] -- {}'.format(i, card))

        decisao = input('Qual operação você deseja realizar? ')
        
        if decisao == '0':
            soma = num1 + num2
            print('{} Esse é o resultado da soma de {} com {}'.format(soma, num1, num2))

        elif decisao == '1':
            sub = num1 - num2
            print('{} Esse é o resultado da subtração de {} com {}'.format(sub, num1, num2))

        elif decisao == '2':
            mult = num1 * num2
            print('{} Esse é o resultado da multiplicação de {} com {}'.format(mult. num1, num2))

        elif decisao == '3' and num2 != 0:
            div = num1 / num2
            print('{} Esse é o resultado da divisão de {} com {}'.format(div, num1, num2))
        
        elif decisao == '3' and num2 == 0:
            print('0 Não pode realizar essa operação onde ele está!')

        else:
            print('Esse valor não está disponível.')
    except:
        print('Você não digitou um número!')
        
        print('Digite 1 para continuar | Digite 0 para finalizar')

        if int(input()) == 0:
            print('Volte sempre!!!')
            break