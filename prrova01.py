temp = float(input())
estado_do_paciente = str(input()).upper()

if temp >= 37 and estado_do_paciente == 'S':
    print('Exames Especiais', end='')

elif temp >= 37 and estado_do_paciente == 'N':
    print('Exames Basicos', end='')

elif temp < 37 and estado_do_paciente == 'N':
    print('Liberado', end='')

elif temp < 37 and estado_do_paciente == 'S':
    print('Exames Basicos', end='')

else:
    print('Erro', end='')