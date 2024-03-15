total_arrecadado = 0
meses_futuros = 0
while True:
    valor = int(input())
    if valor <= 0:
        break
    op_doacao = 0
    while True:
        op_doacao = int(input())
        if op_doacao == 1 or op_doacao == 2:
            break
        else:
            print('Valor invalido')
            continue
    meses = 0
    if op_doacao == 2:
        while True:
            meses = int(input())
            if meses < 2 or meses > 12:
                print('Favor digitar valor entre 2 e 12, inclusive')
                continue
            else:
                break
        meses_futuros += valor * meses - valor
    total_arrecadado += valor
        
print('Total arrecadado para agora: R$ {:.2f}'.format(total_arrecadado))      
print('Total arrecadado para meses futuros: R$ {:.2f}'.format(meses_futuros))