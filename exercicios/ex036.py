peso = float(input('Informe o seu peso em KG: '))
altura = float(input('Informe a sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC: {imc:.1f}')
    print('Classificação: Magreza!')
    print('Grau de obesidade: 0')
elif imc < 24.9:
    print(f'Seu IMC: {imc:.1f}')
    print('Classificação: Normal!')
    print('Grau de obesidade: 0')
elif imc < 29.9:
    print(f'Seu IMC: {imc:.1f}')
    print('Classificação: Sobrepeso!')
    print('Grau de obesidade: I')
elif imc < 39.9:
    print(f'Seu IMC: {imc:.1f}')
    print('Classificação: Obesidade!')
    print('Grau de obesidade: II')
else:
    print(f'Seu IMC: {imc:.1f}')
    print('Classificação: Obesidade grave!!!')
    print('Grau de obesidade: III')