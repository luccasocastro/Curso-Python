# quebrando um número inteiro
# ex: Digite um número: 6.127
# o número 6.127 tem a parte inteira 6
from math import trunc 
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))
