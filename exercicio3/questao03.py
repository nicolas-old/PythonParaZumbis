qtdanos = 0
populacaoA = 80000
populacaoB = 200000
crescimentoA = 0.03
crescimentoB = 0.015

while(populacaoA <= populacaoB):
    populacaoA += (populacaoA * crescimentoA)
    populacaoB += (populacaoB * crescimentoB)
    qtdanos += 1
    print("Populacao A: %i" %populacaoA)
    print("Populacao B: %i" %populacaoB)
    print("Anos: %i" %qtdanos)

print("Sera necessario %i ano(s)" %qtdanos)
