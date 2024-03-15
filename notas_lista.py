n = []
while True:
    print('1 - Adicionar nota \n2 - Imprimir notas \n3 - Remover primeira instância de uma nota \n4 - Sair do programa')

    op = int(input())

    if (op == 1):
        nota = int(input('Digite a nota: '))
        n.append(nota)

    elif op == 2:
        for x in n:
            print('Nota: ', x)
    
    elif op == 3:
        nota_para_remover = int(input('Qual nota quer remover? '))
        n.remove(nota_para_remover)

    elif op == 4:
        print('Até logo!')
        break

    else:
        print('Digite uma opção válida!')
        continue
