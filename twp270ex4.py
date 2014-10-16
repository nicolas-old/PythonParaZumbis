notas = []
contador = 0
media = 0
while(contador<4):
    notas.append(float(input("Digite uma nota: ")))
    media = notas[contador]
    contador += 1

print("Notas: ", notas)
print("A media e: %5.2f" %(media/4))
