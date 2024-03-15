p = int(input())
ul = 1
an = 1
if (p == 1) or ( p == 2):
    print('1')
else:
    cont = 3
    while cont <= p:
        termo = ul + an
        ul = an
        an = termo
        cont += 1
    print(termo)