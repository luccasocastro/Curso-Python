print('='*5 + 'CASTRO BUY' + '='*5)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
op = int(input('[ 1 ] à vista dinheiro/cheque\n'
               '[ 2 ] à vista cartão\n'
               '[ 3 ] 2x no cartão\n'
               '[ 4 ] 3x ou mais no cartão\n'
               'Qual a opção?: '))

if op == 1:
    total = preco - (preco * 10/100)
    print(f'Preço final com 10% de desconto: R${total:.2f}')
elif op == 2:
    total = preco - (preco * 5/100)
    print(f'Preço final com 5% de desconto: R${total:.2f}')
elif op == 3:
    total = preco/2
    print(f'Não oferecemos desconto para esta opção...')
    print(f'Preço final: 2x R${total:.2f}')
elif op == 4:
    tparc = int(input('Deseja parcelar em quantas vezes? '))
    total = preco + (preco * 20/100)
    parc = total/tparc
    print(f'Preço final: {tparc}x R${parc:.2f}, total: R${total:.2f}')


