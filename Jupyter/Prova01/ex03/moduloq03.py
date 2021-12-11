from datetime import date

class BatimentosCardiacos:
    def __init__(self, nome:str, sobrenome:str, dia:int, mes:int, ano:int) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__dia_nascimento = dia
        self.__mes_nascimento = mes
        self.__ano_nascimento = ano
    
    def setNome(self, nome:str):
        self.__nome = nome
    
    def getNome(self) -> str:
        return self.__nome
    
    def setSobrenome(self, sobrenome:str):
        self.__sobrenome = sobrenome
    
    def getSobrenome(self) -> str:
        return self.__sobrenome
    
    def setDia(self, dia:int):
        self.__dia_nascimento = dia
    
    def getDia(self) -> int:
        return self.__dia_nascimento
    
    def setMes(self, mes:int):
        self.__mes_nascimento = mes
    
    def getMes(self) -> int:
        return self.__mes_nascimento
    
    def setAno(self, ano:str):
        self.__ano_nascimento = ano
    
    def getAno(self) -> int:
        return self.__ano_nascimento

def calculaAno(nascimento):
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    return idade

def frequenciaMaxima(idade) -> int:
    return 220 - idade

def fcAlvo(freqMaxima) -> float:
    return freqMaxima * 0.85

def menu(lista):
    c = 0
    print('=-'*15)
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('=-'*15)
    opcao = int(input('Informe a opção desejada: '))
    return opcao

def mostraDados(p: BatimentosCardiacos):
    print(f'Nome: {p.getNome()} {p.getSobrenome()}')
    print(f'Idade: {calculaAno(date(p.getAno(), p.getMes(), p.getDia()))}')