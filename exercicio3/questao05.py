def gcd(a,b):
    while(b!=0):
        t=b
        b = a % b
        a = t
    return a

a = int(input("digite o primeiro numero:"))
b = int(input("digite o segundo numero:"))
print(gcd(a,b))
