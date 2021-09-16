class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, name):
        self._nome = name.lower()
    
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self,valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        
        self._preco = valor

p1 = Produto('CAMISETA', 97)
p1.desconto(17)

p2 = Produto('SHORTS', 'R$63')
p2.desconto(17)

print(f'{p1.nome}, Valor: {p1.preco:.2f}')
print(f'{p2.nome}, Valor: {p2.preco:.2f}')



