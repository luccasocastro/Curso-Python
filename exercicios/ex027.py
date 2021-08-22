v = float(input('Informe a velocidade: '))
if v > 80:
    multa = (v-80)*7
    print('Você está acima da velocidade!! Pagará uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
