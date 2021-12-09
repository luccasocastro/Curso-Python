class Pais:
    def __init__(self, codigo: str, nome: str, populacao: float, dimensao: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__fronteiras = []
    
    # auxiliar
    def mostraInformacoes(self) -> None:
        print(self.__codigo)
        print(self.__nome)
        print(self.__populacao)
        print(self.__dimensao)

    def setFronteiras(self, fronteira):
        self.__fronteiras.append(fronteira)
    
    def getFronteiras(self):
        return self.__fronteiras

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

def mostraFronteiras(p: Pais):
    fronteiras = p.getFronteiras()
    for i in fronteiras:
        print(f'-> {i.getNome()}')

def limitrofe(p1: Pais, p2: Pais):
    cont = 0
    for i in p1.getFronteiras():
        for j in p2.getFronteiras():
            if i == j:
                cont += 1
    
    if cont > 0:
        print(f'{p1.getNome()} é limítrofe de {p2.getNome()}')
    else:
        print(f'{p1.getNome()} não é limítrofe de {p2.getNome()}')
    print('\n')
        
def densidade(p: Pais):
    pop = p.getPopulacao()
    dim = p.getDimensao()
    densidade = pop/dim
    print(f'{p.getNome()} tem densidade de {densidade:.2f} h/Km²')

def addFronteiras(p: Pais, f: Pais):
    if f.getCodigo() != p.getCodigo():
        p.setFronteiras(f)
    else:
        print('Um país ñ pode fazer fronteira com ele mesmo!')

def ordemAlfabetica(paises):
    nomes = []
    for i in paises:
        nomes.append(i.getNome())
    
    nomes.sort()
    print('Países em ordem alfabética:')
    print(nomes)

def menu(lista):
    c = 1
    print('=-'*15)
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('=-'*15)