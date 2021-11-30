class Pais:
    nome = ''
    populacao = 0
    dimensao = 0

    def leDados(self):
        self.nome = str(input('Informe o nome do País: '))
        self.populacao = float(input('Informe a populacao do País: '))
        self.dimensao = float(input('Informe a dimensão do País: '))
    
    def mostraDados(self):
        print('=-'*5)
        print(self.nome)
        print(self.populacao)
        print(self.dimensao)
        print('\n')

class Continente:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.paises = None
    
    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, nome: str):
        self.__nome = nome
    
    def setPaises(self, paises):
        self.paises = paises
    
    def getPaises(self):
        return self.paises
    
    
