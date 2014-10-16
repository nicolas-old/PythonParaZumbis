sdata = raw_input("Digite a data: ")
data = sdata.split('/')
meses = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho',
         'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

print("O mes que voce digitou foi %s" %(meses[int(data[1])-1]))
