from moduloq01 import *

paises = []
paises.append(Pais('BRA', 'Brasil', 300.800, 800.900))
paises.append(Pais('ARG', 'Argentina', 200.500, 600.100))
paises.append(Pais('PAR', 'Paraguai', 10.200, 20.600))
paises.append(Pais('PEU', 'Peru', 100.500, 200.500))

addFronteiras(paises[0], paises[1])
addFronteiras(paises[0], paises[2])
mostraFronteiras(paises[0])
ordemAlfabetica(paises)