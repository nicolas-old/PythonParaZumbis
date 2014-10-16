import random
def embaralha(s):
    lista = list(s)
    random.shuffle(lista)
    return  ''.join(lista)

outralista = embaralha('nicolas')

print(outralista)
