num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print('Os números são iguais')
