valor = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos deseja pagar: '))
prestação = valor/(anos*12)
valMax = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))
if prestação <= valMax:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
