'''l = ['abc', ['a', 'b', 'c'], 'd', ['a',['abc', 'd']]]
c = 0
for e in l:
    c +=len(e)

print(c)'''
# sequencia de fibbonnaci
"""n = 10
aux = [0,1]
for i in range(2, n):
    aux.append(aux[i - 1] + aux[ i - 2])


print(aux)"""

t = 'ngcpftqo'
aux = ''

for i in range(len(t)):
    if ord(t[i]) < 120:
        aux += chr(ord(t[i]) + 2)
    else:
        if ord(t[i]) == 120:
            aux += 'a'
        else:
            aux += 'b'

print(aux)