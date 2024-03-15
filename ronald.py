n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
print('Media: {:.1f}'.format(media))
if(media >= 7):
    print('Aluno aprovado.')
elif(media < 5.0):
    print('Aluno reprovado.')
elif (5.0 < media < 7.0):
    print('Aluno em exame.')
    pontuacao = float(input())
    notadoexame = (media + pontuacao) / 2
    print('Nota do exame: {:.1f}'.format(pontuacao))
    if (notadoexame >= 5.0):
        print("Aluno aprovado.")
        print('Media final: {:.1f}'.format(notadoexame))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(notadoexame))