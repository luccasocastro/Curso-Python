class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            print(self.__somar(num1, num2))
        elif op == '-':
            print(self.__subtrair(num1, num2))
        else:
            print('Opção inválida!')

    def __somar(self, n1, n2):
        return n1+n2

    def __subtrair(self, n1, n2):
        return n1-n2