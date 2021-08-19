dias = int(input('Informe a qntd de dias do aluguel: '))
km = float(input('Quantos Km rodados?: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
