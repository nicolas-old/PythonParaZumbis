qtd=0
with(open('listaTelefonica.txt')) as f:
    linhas = f.readlines()
    for telefones in linhas:
      for telefone in   telefones.rstrip().split(' '):
        if(telefone[0] != telefone[len(telefone)-1]):
            total = 0
            for numero in telefone:
                if(numero != '' and numero != ' '):
                    total += int(numero)
            if(total%2==0):
                existeIgual = False
                for contador in range(len(telefone)):
                    if(telefone[contador] == telefone[contador-1]):
                        existeIgual = True
                if(not existeIgual):
                    print telefone
                    qtd+=1
print qtd
