import random
i=0
lista=[]
while(i<15):
    valor = random.randint(10,100)
    if valor not in lista:
        lista.append(valor)
        i+=1
lista.sort()
print lista
