lista = []

for _ in range(5):
    num = int(input())
    lista.append(num)

par = None
indice = -1
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par = lista[i]
        indice = 1

print("Ultimo par: ",par)
print("Indice do ultimo par: ",indice)