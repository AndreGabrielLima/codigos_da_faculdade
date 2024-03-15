a1 = float(input())
p1 = float(input())
a2 = float(input())
p2 = float(input())

unidade1 = (a1 * 0.2) + (p1 * 0.8)
unidade2 = (a2 * 0.2) + (p2 * 0.8)

resultado = (unidade1 + unidade2) / 2

if a1 == -1 or p1 == -1 or a2 == -1 or p2 == -1:
   print('ND: consultar escolaridade.', end='')

elif resultado < 4:
    print('Reprovado: {:.1f}.'.format(resultado), end='')

elif resultado >= 7.0:
    print('Aprovado: {:.1f}.'.format(resultado), end='')

else:
    nota_final = float(input())
    resultado_final = (unidade1 + unidade2 + nota_final) / 3
    if nota_final == -1:
        print('ND: consultar escolaridade.', end='')
    elif resultado_final < 4.0:
        print('Reprovado: %.1f.' % resultado_final, end='')
    else:
        print('Aprovado na Final: %.1f.' % resultado_final, end='')