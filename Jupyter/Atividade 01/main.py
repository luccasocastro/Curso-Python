so = ['Windows','Unix','Linux','Netware','Mac OS','Outro']
votos = []
total = 0
mais_votos = 0
mais_votado = ''

print('Informe a qntd de votos:')
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
for i in range(0,6):
    votos.append(float(input(f'{so[i]}:')))

for i in range(0,6):
    total += votos[i]
    if votos[i] > mais_votos:
        mais_votos = votos[i]
        mais_votado = so[i]

porc = (mais_votos * 100)/total

print('Total=',total)
print(f'O sistema com mais votos foi {mais_votado} com {mais_votos} votos, equivalentes a {porc:.1f}% dos votos')