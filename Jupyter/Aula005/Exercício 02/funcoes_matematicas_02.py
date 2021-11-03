'''Faça uma nova função no módulo acima que calcule o fatorial e o somatório em conjunto e retorne ambos os valores. Essa nova função, deve ser chamada no segundo programa como descrito acima.'''

def fat_sum(n1:int, n2:int) -> int:
    res = 1
    for i in range(1,n1+1):
        res *= i
    
    return res, n1+n2


