def epar(x):
    return x%2==0

print(epar(13))
print(epar(12))

def fat(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f



print(fat(10))

for i in range(10): print(fat(i))
