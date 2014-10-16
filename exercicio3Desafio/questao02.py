qtdNotas = [0, 0, 0, 0, 0, 0]
valorConta = 0
valorPago  = 0

while(valorConta == valorPago or valorPago < valorConta):
    valorConta = int(input('Digite o valor da conta: '))
    valorPago  = int(input('Digite o valor pago:'))

saldoDevedor = valorPago - valorConta
while(saldoDevedor>0):
    if(saldoDevedor-50>=0):
        saldoDevedor-=50
        qtdNotas[0] += 1
    else:
        if(saldoDevedor-20>=0):
            saldoDevedor-=20
            qtdNotas[1] +=1
        else:
            if(saldoDevedor-10>=0):
                saldoDevedor-=10
                qtdNotas[2] +=1
            else:
                if(saldoDevedor-5>=0):
                    saldoDevedor-=5
                    qtdNotas[3] +=1
                else:
                    if(saldoDevedor-2>=0):
                        saldoDevedor-=2
                        qtdNotas[4]+=1
                    else:
                        if(saldoDevedor-1>=0):
                            saldoDevedor-=1
                            qtdNotas[5]+=1


print('Total de notas de 50: %i' %(qtdNotas[0]))
print('Total de notas de 20: %i' %(qtdNotas[1]))
print('Total de notas de 10: %i' %(qtdNotas[2]))
print('Total de notas de  5: %i' %(qtdNotas[3]))
print('Total de notas de  2: %i' %(qtdNotas[4]))
print('Total de notas de  1: %i' %(qtdNotas[5]))
