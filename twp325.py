#Leia mensagem.txt e escreva cripto.txt trocando todas as vogais por '*'
saida = open('cripto.txt','w')

with(open('mensagem.txt')) as f:
    palavra = f.readlines()
    for letra in palavra:
        if(letra in 'aeiou'):
            letra = '*'
            saida.write(letra)
saida.close()
