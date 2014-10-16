palavra = raw_input('Digite uma palavra: ')

if(palavra == palavra[::-1]):
    print("A palavra %s e palindrome!" %palavra)
else:
    print("A palavra %s nao e palindrome!" %palavra)
