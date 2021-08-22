from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 22)
print('Olá, vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-' * 22)
num = int(input('Qual o número que eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if num == pc:
    print('PARABÉNS!!! Você acertou!!')
else:
    print('GANHEI!!! Eu pensei no número {} não no {}'.format(pc, num))

