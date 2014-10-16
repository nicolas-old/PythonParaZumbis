import random
menor = 100
maior = 0
lista = []
for contador in range(10):
    valor = random.randint(1,100)
    lista.append(valor)
    if(maior<valor):
        maior = valor
    if(menor>valor):
        menor = valor

lista.sort()
print(lista)
print('Menor: %d' %menor)
print('Maior: %d' %maior)

