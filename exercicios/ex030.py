num = int(input('Informe um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Escolha uma opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')