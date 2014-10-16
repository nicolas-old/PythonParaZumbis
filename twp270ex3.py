contador = 0
matriz = []

while(contador<10):
    matriz.append(float(input("Digite um valor:")))
    contador += 1
contador -= 1
while(contador>=0):
    print(matriz[contador])
    contador -= 1
