def medias(numbers):
    n1, n2, n3, n4 = map(float, numbers.strip().split(' '))
    m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)
    print('Media: {:.1f}'.format(m))
    if m >= 7:
        return 'Aluno aprovado.'
    elif m < 5.0:
        return 'Aluno reprovado.'
    elif 5.0 <= m < 7.0:
        print('Aluno em exame.')
        e = float(input())
        print('Nota do exame: {:.1f}'.format(e))
        if (m + e) / 2 >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        return 'Media final: {:.1f}'.format((m + e) / 2)


med = input()
print(medias(med))