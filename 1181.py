matriz = []

l = int(input())
op = input()

N = 12

for i in range(N):
    linha = []
    for j in range(N):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for num in matriz[l]:
    soma += num
if op == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/N))
