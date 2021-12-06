from moduloq02 import *
africa = Continente('África')
print(africa.getNome())

lista_paises = []

qntd = int(input('Informe a qntd de paises: '))
for i in range(0, qntd):
    p = Pais()
    p.leDados()
    lista_paises.append(p)

for i in range(0, qntd):
    addPais(africa, lista_paises[i])

for p in africa.paises:
    p.mostraDados()

dTotal = dimTotal(africa)
print(f'Dim Total: {dTotal}')

paism = menorPop(africa, qntd)
print(f'O país com menor população é {paism.getNome()}')