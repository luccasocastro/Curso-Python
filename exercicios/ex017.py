# sorteando um item na lista
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
lista = [n1, n2, n3]
escolhido = choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))
