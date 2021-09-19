from datetime import datetime

ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
ano = int(input('Informe seu ano de nascimento: '))
idade = ano_atual-ano

if idade == 18:
    print(f'Você tem {idade} anos, já está na hora de se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos, já deveria ter se alistado...')
else:
    alistamento = ano + 18
    print(f'Você tem {idade} anos \nVocê deverá se alistar em {alistamento}!')
