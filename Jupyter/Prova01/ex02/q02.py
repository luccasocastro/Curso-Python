from moduloq02 import *

while True:
    op = menu(['Sair', 'Criar Continente', 'Adicionar Países', 'Dimensão Total', 'População Total', 'País com Maior População', 'País com Menor População', 'País com Maior Dimensão Territorial', 'País com Menor Dimensão Territorial', 'Razão Territorial'])

    if op == 0:
        print('Goodbye!!!')
        break
    elif op == 1:
        print('Criar Continente: ')
        nome = str(input('Informe o nome do Continente: '))
        c = Continente(nome)

    elif op == 2:
        qntd = int(input('Quantos Países deseja adicionar? '))
        for i in range(0, qntd):
            p = Pais()
            p.leDados()
            addPais(c, p)

    elif op == 3:
        print('Dimensão Total do Continente: ')
        print(f'{dimTotal(c)} Km')

    elif op == 4:
        print('População Total do Continente: ')
        print(f'{popTotal(c)} Habitantes')

    elif op == 5:
        print('País com Maior População: ')
        p = maiorPop(c)
        print(f'-> {p.getNome()}')
        print(f'-> População: {p.getPopulacao()}')

    elif op == 6:
        print('País com Menor População: ')
        p = menorPop(c, qntd)
        print(f'-> {p.getNome()}')
        print(f'-> População: {p.getPopulacao()}')

    elif op == 7:
        print('País com Maior Dimensão: ')
        p = maiorDim(c)
        print(f'-> {p.getNome()}')
        print(f'-> Dimensão: {p.getDimensao()}')

    elif op == 8:
        print('País com Menor Dimensão: ')
        p = menorDim(c, qntd)
        print(f'-> {p.getNome()}')
        print(f'-> Dimensão: {p.getDimensao()}')

    elif op == 9:
        razaoTerritorial(c, qntd)