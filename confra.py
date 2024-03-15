'''valor = float(input())
sindi = int(input())
soma = 0
for i in range(sindi):
    nome = str(input())
    valor_dado = float(input())
    soma += valor_dado
    media = soma /sindi
print('{} '.format(media))'''

m_n = ''
m_v = -1
soma = 0

vt = float(input())
n_p = int(input())
if n_p == 0:
    print('Nao ha conta ou funcionario suficiente para pagar a conta.', end='')
else:    
    for i in range(n_p):
        p = input()
        v = float(input())
        soma += v
        if (v > m_v):
            m_v = v
            m_n = p
    print('%s pagou R$ %.1f' %(m_n, m_v))
    if vt > soma:
        print('Valor insuficiente: - R$ %.1f' %(vt - soma), end='')
    elif vt < soma:
        print('Valor excedente: + R$ %.1f' %(soma - vt), end='')

    else:
        print('Conta paga!', end='')