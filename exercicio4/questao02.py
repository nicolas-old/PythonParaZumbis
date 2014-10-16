import random
lista = []
par = []
impar = []

for i in range(20):
    valor = random.randint(1,100)
    lista.append(valor)
    if(valor % 2 == 0):
        par.append(valor)
    if(valor % 3 == 0):
        impar.append(valor)

lista.sort()
par.sort()
impar.sort()

print(lista)
print(par)
print(impar)
