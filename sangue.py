idade = int(input())
sexo = str(input()).upper()
peso = float(input())
doacoes_do_ano = int(input())
ultima_doacao = int(input())
mes_atual = int(input())

if (idade >= 18 or idade <60) and peso > 50.0:
    if sexo == 'M':
        if doacoes_do_ano > 0 or doacoes_do_ano < 5:
            
            intervalo = mes_atual - ultima_doacao
            
            if intervalo >= 2:
                print('Apto(a).', end='')
            else:
                print('Inapto(a).', end='')
        elif doacoes_do_ano == 0:
            print('Apto(a)', end='')
        else:
            print('Inapto(a)', end='')

    if sexo == 'F':
        if doacoes_do_ano > 0 or doacoes_do_ano < 4:
            
            intervalo = mes_atual - ultima_doacao
            
            if intervalo >= 3:
                print('Apto(a).', end='')
            else:
                print('Inapto(a).', end='')
        elif doacoes_do_ano == 0:
            print('Apto(a)', end='')
        else:
            print('Inapto(a)', end='')
else:
    print('Inapto(a).', end='')
            