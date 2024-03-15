while True:
    try:
        valor = int(input())

        if 3 <= valor <= 70:
            matriz = []

            for i in range(valor):
                l = []
                for j in range(valor):
                    l.append(3)
                matriz.append(l)

            for i in range(valor):
                matriz[i][i] = 1
                matriz[i][valor - 1 - i] = 2

            for i in range(valor):
                for j in range(valor):
                    print(matriz[i][j], end='')
                print()

    except EOFError:
        break