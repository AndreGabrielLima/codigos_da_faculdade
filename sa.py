idade = int(input())
sexo = str(input()).upper()
peso = float(input())
doacoes = int(input())
if doacoes != 0:
    mes_ult_doacao = int(input())
mes = int(input())

if (idade >= 18 and idade < 60) and peso > 50.0:
    if sexo == 'M':
        if doacoes > 0 and doacoes < 5:
            intervalo = mes - mes_ult_doacao
            if intervalo >= 2:
                print('Apto(a).', end='')
            else:
                print('Inapto(a).', end = '')
        elif doacoes == 0:
            print('Apto(a).', end = '')
        else:
            print('Inapto(a).', end='')
    if sexo == 'F':
        if doacoes > 0 and doacoes < 3:
            intervalo = mes - mes_ult_doacao
            if intervalo >= 3:
                print('Apto(a).', end='')
            else:
                print('Inapto(a).', end='') 
        elif doacoes == 0:
            print('Apto(a).', end='')
        else:
            print('Inapto(a).', end='')
else:
    print('Inapto(a).', end='')