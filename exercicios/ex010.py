preco = float(input('Informe o preço: '))
desconto = preco - (preco*5/100)
print('R${:.2f} com 5% de desconto é R${:.2f}'.format(preco, desconto))

