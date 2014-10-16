notas = []
contador = 0
nota = 0
while(contador<10):
    nota = int(input('Digite uma nota: '))
    if(nota <  0 or nota > 10):
        print('Digite novamente, o valor esta %d invalido' %nota)
    else:
        notas.append(nota)
        contador += 1

print("Notas lidas: ", notas)
