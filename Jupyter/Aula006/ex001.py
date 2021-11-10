# Exercício 01
# Faça um programa que leia 5 números inteiros e os coloque em uma lista.
# Após, pergunte ao usuário uma posição na lista e apresente o valor que
# está nessa posição. Faça o tratamento de erro para a leitura dos números
# e também para a posição na lista.

lista = []
for i in range(0,5):
    try:
        lista.append(int(input('Informe um número: ')))
    except Exception as erro:
        print(f'Informação inválida!!! Erro: {erro.__class__}')

try:
    pos = int(input('Que posição deseja visitar?: '))
    print(f'Posição solicitada: {lista[pos]}')
except:
    print('Posição inválida')



