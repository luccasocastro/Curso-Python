from moduloq01 import *

brasil = Pais('BRA', 'Brasil', 300.800, 800.900)
argentina = Pais('ARG', 'Argentina', 200.500, 600.100)
paraguai = Pais('PAR', 'Paraguai', 10.200, 20.600)
peru = Pais('PEU', 'Peru', 100.500, 200.500)

fronteiras1 = ['argentina', 'paraguai']
fronteiras2 = ['brasil']

brasil.setFronteiras(fronteiras1)
peru.setFronteiras(fronteiras2)

mostraFronteiras(brasil)
mostraFronteiras(peru)

limitrofe(brasil, peru)

densidade(brasil)