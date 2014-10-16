numero=int(input('Digite o numero: '))
listaPrimos = []
divisores = []
for numeroPrimo in range(numero):
        i = numeroPrimo
        if(i>0):
            qtdDivisores = 0
            while i >= 1 and qtdDivisores <= 2:
                if(numeroPrimo % i == 0):
                    listaPrimos.append(numeroPrimo)
                    qtdDivisores += 1
                i-=1
print listaPrimos
i = 0
while(numero!=1):
    if(numero % listaPrimos[i]==0):
        divisores.append(listaPrimos[i])
        numero = numero/listaPrimos[i]
        i = -1
    i+=1

print divisores
