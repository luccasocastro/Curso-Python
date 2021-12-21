from moduloq03 import *
from datetime import date

nome = str(input('Informe o seu nome: '))
sobrenome = str(input('Informe seu sobrenome: '))
dia = int(input('Informe seu dia de nascimento: '))
mes = int(input('Informe seu mês de nascimento: '))
ano = int(input('Informe seu ano de nascimento: '))

p1 = BatimentosCardiacos(nome, sobrenome, dia, mes, ano)
idade = calculaAno(date(p1.getAno(), p1.getMes(), p1.getDia()))
freqMax = frequenciaMaxima(idade)

print('=-'*10)
print('\tSTATUS:')
print('=-'*10)
print(f'Nome completo: {p1.getNome()} {p1.getSobrenome()}')
print(f'Idade: {idade} anos')
print(f'Frequência cardíaca máxima: {freqMax}')
print(f'Frequência cardíaca alvo: {fcAlvo(freqMax)}')
print('=-'*10)
