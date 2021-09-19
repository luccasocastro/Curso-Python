n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informa a segunda nota: '))
m = (n1+n2)/2

if m >= 7:
    print(f'Sua média é {m:.1f} e você está APROVADO!!!')
elif m < 7 and m > 5:
    print(f'Sua média é {m:.1f} e você está de RECUPERAÇÃO!!!')
else:
    print(f'Sua média é {m:.1f} e você está REPROVADO!!!')