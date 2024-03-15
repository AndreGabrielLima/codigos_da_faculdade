n = int(input())
for i in range(n):
    lista = str(input()).strip().split()
    cut_list = sorted(set(lista))
    print(' '.join(cut_list))