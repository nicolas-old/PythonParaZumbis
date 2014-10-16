import random
vetor1 = []
vetor2 = []
juncao = []

for i in range(10):
    vetor1.append(random.randint(1,100))
    vetor2.append(random.randint(1,100))

    juncao.append(vetor1[len(vetor1)-1])
    juncao.append(vetor2[len(vetor2)-1])

print(vetor1)
print(vetor2)
print(juncao)
