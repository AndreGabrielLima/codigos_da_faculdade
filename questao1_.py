notas_dos_alunos = []

for i in range(1, 11):
    notas = float(input())

    notas_dos_alunos.append(notas)

soma = sum(notas_dos_alunos)
quant = len(notas_dos_alunos)
media = soma / quant

print('{:.2f}'.format(media))

for i in range(len(notas_dos_alunos)):
    if notas_dos_alunos[i] <= media:
        print(i + 1,' ', end='')
