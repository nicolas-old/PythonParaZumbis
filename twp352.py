from tatu_twp352 import Cliente
from tatu_twp352 import Conta

joao = Cliente('Joao da Silva', '7777-55555')
maria = Cliente('Maria da Silva', '5555')

print('Nome: %s. Telefone: %s', (joao.nome, joao.telefone))
print('Nome: %s. Telefone: %s', (maria.nome, maria.telefone))

conta1 = Conta([joao], 10000)
conta2 = Conta([joao,maria], 599)

conta1.resumo()
conta2.resumo()

