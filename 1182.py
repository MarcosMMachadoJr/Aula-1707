matriz = []

c = int(input())
op = input()

N = 3

for i in range(N):
    coluna = []
    for j in range(N):
        coluna.append(float(input()))
    matriz.append(coluna)

soma = 0
for l in range(len(matriz[c])):
    soma += matriz[l][c]

if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/N))
