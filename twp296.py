import random
def aleatorio():
    return random.randint(10,100)

lista = []

for i in range(15):
    lista.append(aleatorio())

print lista


lista = []
for k in range(15):
    lista.append(random.randint(10,100))
print lista
