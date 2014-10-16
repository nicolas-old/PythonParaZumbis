notas = [5, 7, 10, 4, 3]
contador = 1
media = notas[0]
while (contador<5):
    media =(media + notas[contador]) / 2
    contador = contador + 1

print media


media = 0
contador = 0
while(contador<5):
    media += notas[contador]
    contador += 1

print("Media: %5.2f" %(media/contador))
