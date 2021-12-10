class Pais:
    def leDados(self):
        self.nome = str(input('Informe o nome do País: '))
        self.populacao = float(input('Informe a populacao do País: '))
        self.dimensao = float(input('Informe a dimensão do País: '))
    
    def mostraDados(self):
        print('=-'*5)
        print(self.nome)
        print(self.populacao)
        print(self.dimensao)

    def getNome(self) -> str:
        return self.nome
    
    def setNome(self, nome: str):
        self.nome = nome
    
    def getPopulacao(self) -> float:
        return self.populacao
    
    def setPopulacao(self, populacao: float):
        self.populacao = populacao
    
    def getDimensao(self) -> float:
        return self.dimensao
    
    def setDimensao(self, dimensao: float):
        self.dimensao = dimensao

class Continente:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.paises = []
    
    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, nome: str):
        self.__nome = nome
    
    def setPaises(self, pais):
        self.paises.append(pais)
    
    def getPaises(self):
        return self.paises
    
def addPais(c: Continente, p: Pais):
    c.setPaises(p)

def dimTotal(c: Continente) -> float:
    paises = c.getPaises()
    total = 0
    for i in paises:
        total += i.getDimensao()
    
    return total

def popTotal(c: Continente) -> float:
    paises = c.getPaises()
    total = 0
    for i in paises:
        total += i.getPopulacao()
    
    return total

def maiorPop(c: Continente) -> Pais:
    paises = c.getPaises()
    maior = 0
    paism = None

    for i in paises:
        if i.getPopulacao() > maior:
            maior = i.getPopulacao()
            paism = i
    
    return paism

def menorPop(c: Continente, qntd: int) -> Pais:
    paises = c.getPaises()
    menor = paises[0]

    for i in range(1, qntd):
        if paises[i].getPopulacao() < menor.getPopulacao():
            menor = paises[i]
    
    return menor

def maiorDim(c: Continente) -> Pais:
    paises = c.getPaises()
    maior = 0
    paism = None

    for i in paises:
        if i.getDimensao() > maior:
            maior = i.getDimensao()
            paism = i
        
    return paism

def menorDim(c: Continente, qntd: int) -> Pais:
    paises = c.getPaises()
    menor = paises[0]

    for i in range(1, qntd):
        if paises[i].getDimensao() < menor.getDimensao():
            menor = paises[i]
    
    return menor

def razaoTerritorial(c: Continente, qntd: int):
    p1 = maiorDim(c)
    p2 = menorDim(c, qntd)

    print(f'Razão entre maior e menor País é: {p1.getDimensao()}/{p2.getDimensao()}')

def menu(lista):
    c = 0
    print('=-'*15)
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('=-'*15)
    opcao = int(input('Informe a opção desejada: '))
    return opcao