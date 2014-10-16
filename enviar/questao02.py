informacaoCorreta = False
nomedeusuario = ""
senha = ""

while(not informacaoCorreta):
    nomedeusuario = raw_input("Digite o nome de usuario: ")
    senha = raw_input("Digite a senha: ")
    if(nomedeusuario == senha):
        print("Digite novamente!")
    else:
        informacaoCorreta = True

print("Bem vindo, %s" %nomedeusuario)
