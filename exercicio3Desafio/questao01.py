num = int(input("Digite um numero: "))
start = 1
triangulou = False
while(start<num-3 and not triangulou):
    if((start)*(start+1)*(start+2)==num):
        triangulou = True
    start+=1
print('Triangulou: %s' %triangulou)
