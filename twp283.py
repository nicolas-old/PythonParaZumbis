palavra = raw_input("Digite uma palavra: ")
contador = 0
palavrasubstituida = ''
while(contador < len(palavra)):
    if(palavra[contador:contador+1] in 'aeiou'):
        palavrasubstituida += '*'
    else:
        palavrasubstituida += palavra[contador:contador+1]
    contador += 1
print palavrasubstituida
