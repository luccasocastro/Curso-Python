class ContaCorrente:
    def __init__(self,nconta: int, nome: str, saldo: float) -> None:
        self.nconta = nconta
        self.nome = nome
        self.saldo = saldo
    
    def alterar_nome(self,novo_nome: str) -> None:
        self.nome = novo_nome
    
    def deposito(self, valor: float) -> None:
        self.saldo += valor
    
    def saque(self, valor: float) -> None:
        self.saldo -= valor
    
    def status(self) -> None:
        print('STATUS')
        print('=-=-=-=-=-=-=-=-=-=-=')
        print(f'nº conta: {self.nconta}\nNome: {self.nome}\nSaldo: R${self.saldo}\n')

c1 = ContaCorrente(1111, 'Luccas Castro de Silva', 0)
c1.status()
c1.alterar_nome('Luccas Castro de Souza')
c1.deposito(1.999)
c1.status()