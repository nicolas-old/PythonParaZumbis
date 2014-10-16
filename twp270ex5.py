vetor = []
contador = 0
contadorConsoante = 0

while (contador<10):
    vetor.append(raw_input("Type a string: "))
    if(vetor[contador] not in 'aeiou'):
        contadorConsoante += 1
    contador += 1

print("Existem  %d consoantes" %contadorConsoante)

