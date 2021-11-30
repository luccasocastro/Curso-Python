class Pais:
    def __init__(self, codigo: str, nome: str, populacao: float, dimensao: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
    
    # auxiliar
    def mostraInformacoes(self) -> None:
        print(self.__codigo)
        print(self.__nome)
        print(self.__populacao)

    def getCodigo(self) -> str:
        return self.__codigo

    def setCodigo(self, codigo: str):
        self.__codigo = codigo

    def getNome(self) -> str:
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getPopulacao(self) -> float:
        return self.__populacao

    def setPopulacao(self, populacao: float):
        self.__populacao = populacao
    
    def getDimensao(self) -> float:
        return self.__dimensao
    
    def setDimensao(self, dimensao: float):
        self.__dimensao = dimensao

def verificaIgual(p1: Pais, p2: Pais):
    if p1.getCodigo() == p2.getCodigo():
        print('País 1 é igual ao País 2!')
    else:
        print('País 1 não é igual ao País 2!')

