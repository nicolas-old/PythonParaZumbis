fib = 1
fibPass = 1
num = int(input("Digite a qtd de numeros: "))
while(num>2):
    fibOld = fib
    fib+=fibPass
    fibPass = fibOld
    num-=1

print(fib)
