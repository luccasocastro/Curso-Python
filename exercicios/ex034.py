from datetime import date

ano_atual = date.today().year
ano = int(input('Informe o ano do seu nascimento: '))
idade = ano_atual - ano

if idade <= 9:
    print(f'{idade} anos de idade: categoria MIRIM')
elif idade <= 14:
    print(f'{idade} anos de idade: categoria INFANTIL')
elif idade <= 19:
    print(f'{idade} anos de idade: categoria JÚNIOR')
elif idade <= 25:
    print(f'{idade} anos de idade: categoria SÊNIOR')
else:
    print(f'{idade} anos de idade: categoria MASTER')