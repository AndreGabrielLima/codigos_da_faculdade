hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()

hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final)

minuto_inicial += hora_inicial*60
minuto_final += hora_final*60

tempo = minuto_final - minuto_inicial

if tempo <= 0:
    tempo += 24*60

H = tempo//60
m = tempo%60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(H, m))