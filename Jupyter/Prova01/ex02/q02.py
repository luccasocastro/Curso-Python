from moduloq02 import *
africa = Continente('África')
print(africa.getNome())

lista_paises = []

qntd = int(input('Informe a qntd de paises: '))
for i in range(0, qntd):
    p = Pais()
    p.leDados()
    lista_paises.append(p)

africa.setPaises(lista_paises)

for p in africa.paises:
    p.mostraDados()

