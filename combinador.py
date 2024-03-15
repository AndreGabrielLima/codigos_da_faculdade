valor = int(input())

for i in range(valor):
    string1, string2 = input().strip().split(' ')

    tamanho = min(len(string1), len(string2))
    resposta = ''.join([string1[i] + string2[i] for i in range(tamanho)])
    resposta = resposta + (string1[tamanho:] if tamanho < len(string1) else string2[tamanho:])

    print(resposta)