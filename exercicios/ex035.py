l1 = float(input('Informe o lado 1: '))
l2 = float(input('Informe o lado 2: '))
l3 = float(input('Informe o lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM formar um triângulo!')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO podem formar um triângulo!')