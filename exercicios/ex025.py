nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Prazer em conhecê-lo!!!')
print('Seu primeiro nome é {}\nE o seu último nome é {}'.format(div[0], div[len(div)-1]))

