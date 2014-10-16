numero = int(input('Digite um numero: '))
divisor = numero
qtdDivisor = 0

while(divisor>0 and qtdDivisor <= 2):
    if(numero % divisor == 0):
        qtdDivisor += 1
    divisor -= 1

if(qtdDivisor==2):
    print("O numero digitado %d e primo" %numero)
else:
    print("O numero digitado %d nao e primo" %numero)
