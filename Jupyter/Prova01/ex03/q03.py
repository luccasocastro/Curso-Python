from moduloq03 import *

while True:
    opcao = menu(['Sair', 'Cadastrar Dados', 'Mostrar Dados', 'Frequência Cardíaca Máxima da Pessoa', 'Frequência Cardíaca Alvo da Pessoa'])
    if opcao == 0:
        print('Goodbye!!!')
        break
    elif opcao == 1:
        print('Cadastrando de dados: ')
        nome = str(input('Informe o seu nome: '))
        sobrenome = str(input('Informe seu sobrenome: '))
        dia = int(input('Informe seu dia de nascimento: '))
        mes = int(input('Informe seu mês de nascimento: '))
        ano = int(input('Informe seu ano de nascimento: '))
        p1 = BatimentosCardiacos(nome, sobrenome, dia, mes, ano)

    elif opcao == 2:
        mostraDados(p1)

    elif opcao == 3:
        idade = calculaAno(date(p1.getAno(), p1.getMes(), p1.getDia()))
        freqMax = frequenciaMaxima(idade)
        print(f'A frequência cardíaca máxima de {p1.getNome()} é {freqMax:.2f} Bpm')

    elif opcao == 4:
        print(f'A frequência cardíaca alvo de {p1.getNome()} é {fcAlvo(freqMax):.2f} Bpm')