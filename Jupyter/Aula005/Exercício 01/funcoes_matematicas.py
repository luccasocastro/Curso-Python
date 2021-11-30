'''Faça um programa em Python que tenha um módulo que realize as seguintes funções: fatorial, somatório e potencia de uma base por um expoente. Todos os parâmetros nesses casos devem ser valores inteiros positivos. No caso, faça um segundo programa que faça chamadas às funções do módulo desenvolvido.'''

def fat(num: int) -> int:
    res = 1
    for i in range(1,num+1):
        res *= i
    
    return res

def pot(base:int, expoente:int) -> int:
    return base+expoente, base**expoente


