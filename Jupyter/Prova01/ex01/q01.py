from moduloq01 import *

paises = []

while True:
    op = menu(['Sair','Cadastrar País', 'Verifica Igual', 'Verifica Limítrofe', 'Densidade Populacional', 'Vizinhos Comuns', 'Países Ordem Alfabética', 'Adicionar Fronteira'])
    if op == 1:
        print('Cadastrar País: ')
        codigo = str(input('Informe o código: '))
        nome = str(input('Informe o nome: '))
        populacao = float(input('Informe a população: '))
        dimensao = float(input('Informe a dimensão: '))
        paises.append(Pais(codigo, nome, populacao, dimensao))

    elif op == 2:
        c = 0
        print('Países Cadastrados: ')
        for p in paises:
            print(f'{c} - {p.getNome()}')
            c += 1
        p1 = int(input('Informe o índice do 1º País a ser comparado: '))
        p2 = int(input('Informe o índice do 2º País a ser comparado: '))
        verificaIgual(paises[p1], paises[p2])

    elif op == 3:
        c = 0
        print('Verifica Limítrofe: ')
        for p in paises:
            print(f'{c} - {p.getNome()}')
            c += 1
        p1 = int(input('Informe o índice do 1º País a ser comparado: '))
        p2 = int(input('Informe o índice do 2º País a ser comparado: '))
        limitrofe(paises[p1], paises[p2])

    elif op == 4:
        c = 0
        print('Densidade Populacional: ')
        for p in paises:
            print(f'{c} - {p.getNome()}')
            c += 1
        p = int(input('Informe o índice do País desejado: '))
        densidade(paises[p])

    elif op == 5:
        print('Vizinhos Comuns')
    elif op == 6:
        print('Países Ordem Alfabética')
    elif op == 7:
        c = 0
        print('Adicionar Fronteira: ')
        for p in paises:
            print(f'{c} - {p.getNome()}')
            c += 1
        p = int(input('Informe o índice do País que deseja adicionar uma fronteira: '))
        f = int(input('Informe o índice do País fronteira a ser adicionado: '))
        addFronteiras(paises[p], paises[f])
        
    elif op == 0:
        print('Goodbye!!')
        break
